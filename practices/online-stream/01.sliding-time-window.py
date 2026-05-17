from collections import defaultdict, deque
import heapq
from typing import List, Tuple

class SlidingWindowAggregator:
    def __init__(self, W: int, ttl: int, max_users: int):
        self.W = W
        self.ttl = ttl              # 스킵 가능 (placeholder)
        self.max_users = max_users  # 스킵 가능 (placeholder)

        self.user_q = defaultdict(deque)     # user_id -> deque[(time, value)]
        self.user_sum = defaultdict(float)   # user_id -> rolling sum (may be stale until pruned)
        self.user_count = defaultdict(int)   # user_id -> rolling count
        self.user_ver = defaultdict(int)     # user_id -> version for heap validation

        # (-sum, user_id, version)
        self.topk_heap = []

    def _prune(self, now: int, user_id: str) -> None:
        q = self.user_q[user_id]
        cutoff = now - self.W  # remove time <= cutoff  (윈도우: (now-W, now])
        while q and q[0][0] <= cutoff:
            t, v = q.popleft()
            self.user_sum[user_id] -= v
            self.user_count[user_id] -= 1

        # 필요하면: sum이 0이고 q가 비면 state 정리(메모리 절감)
        # (TTL 스킵 버전에서도 간단히 가능)
        if not q:
            # defaultdict라 del 안 하면 키가 남을 수 있으니 조심스럽게 정리
            if user_id in self.user_sum: del self.user_sum[user_id]
            if user_id in self.user_count: del self.user_count[user_id]
            if user_id in self.user_q: del self.user_q[user_id]
            if user_id in self.user_ver: del self.user_ver[user_id]

    def ingest(self, event_time: int, user_id: str, value: float) -> None:
        # 가정: event_time도 호출 순서상 non-decreasing (아니면 설계가 더 복잡해짐)
        q = self.user_q[user_id]
        q.append((event_time, value))
        self.user_sum[user_id] += value
        self.user_count[user_id] += 1

        # ingest 시점에 해당 유저만 prune (eager per-user)
        self._prune(event_time, user_id)

        # heap 갱신 (stale 허용)
        self.user_ver[user_id] += 1
        ver = self.user_ver[user_id]
        heapq.heappush(self.topk_heap, (-self.user_sum[user_id], user_id, ver))

    def query(self, current_time: int, user_id: str) -> Tuple[float, int]:
        if user_id not in self.user_q:
            return (0.0, 0)
        self._prune(current_time, user_id)
        if user_id not in self.user_q:
            return (0.0, 0)
        return (self.user_sum[user_id], self.user_count[user_id])

    def topk(self, current_time: int, k: int) -> List[Tuple[str, float]]:
        result: List[Tuple[str, float]] = []
        seen = set()

        while self.topk_heap and len(result) < k:
            neg_sum, user_id, ver = heapq.heappop(self.topk_heap)

            # 이미 뽑은 유저면 스킵
            if user_id in seen:
                continue

            # 유저가 이미 삭제됐거나, stale entry면 스킵
            if user_id not in self.user_ver or self.user_ver[user_id] != ver:
                continue

            # current_time 기준으로 prune해서 최신화
            self._prune(current_time, user_id)
            if user_id not in self.user_q:
                continue

            true_sum = self.user_sum[user_id]

            # sum이 prune으로 바뀌었을 수 있으니 heap에 최신 값 재삽입
            self.user_ver[user_id] += 1
            new_ver = self.user_ver[user_id]
            heapq.heappush(self.topk_heap, (-true_sum, user_id, new_ver))

            # 근사 top-k: pop된 후보를 채택
            result.append((user_id, true_sum))
            seen.add(user_id)

        return result
