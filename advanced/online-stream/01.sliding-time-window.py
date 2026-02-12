"""
좋습니다. 지금부터 **인터뷰어 모드**로 진행하겠습니다. (한국어로만)

---

## 문제 1개 (Medium–Hard): TTL + Sliding-Time Window + Per-User State + Memory/Eviction

당신은 **실시간 추천/사기탐지용 온라인 피처 집계기**를 구현 중입니다. 이벤트 스트림이 들어오고, 모델 서빙에서 아주 낮은 지연으로 피처를 조회해야 합니다.

### 이벤트

각 이벤트는 아래 형태입니다:

* `(event_time: int, user_id: str, value: float)`

### 요구 피처

각 user에 대해 다음 두 피처를 제공합니다.

1. **SumW(user, t)**: 시각 `t`에서, **최근 W초**(t-W, t] 동안의 `value` 합
2. **CountW(user, t)**: 같은 윈도우 동안의 이벤트 개수

### API (인터뷰에서 흔한 스타일로 일부 의도적으로 덜 명확)

다음 클래스를 구현하세요.

* `__init__(W: int, ttl: int, max_users: int)`
* `ingest(event_time: int, user_id: str, value: float) -> None`
* `query(current_time: int, user_id: str) -> tuple[float, int]`

  * 반환: `(SumW, CountW)` 없으면 `(0.0, 0)`
* `topk(current_time: int, k: int) -> list[tuple[str, float]]`

  * 시각 `current_time`에서 **SumW가 큰 user 상위 k명**을 `(user_id, SumW)`로 반환

### 핵심 제약/트위스트 (현업 느낌)

* `current_time`은 `ingest`와 `query/topk` 호출 전반에서 **non-decreasing** 입니다.
* 이벤트는 대부분 현재 시각 근처지만, **약간의 지연 도착(out-of-order)** 이 있을 수 있습니다.
  단, 지연 범위는 작다고만 말해줍니다(예: “몇 초 수준”). 정확한 값은 당신이 가정해야 합니다.
* 사용자 수는 **수백만** 가능.
* 메모리는 제한적이라서:

  * **max_users**를 넘으면 eviction 필요
  * 그리고 user 상태는 **ttl** 동안 활동이 없으면 자동 제거해야 함
* `topk()`는 매번 모든 유저를 스캔하면 안 됩니다(너무 느림).
  **정확한 top-k**를 요구하는지, **근사 허용**인지도 명확히 안 줍니다 → 당신이 질문/가정해야 합니다.

---

## 지금 당신 차례 (Step 2)

코딩 들어가기 전에 **가정(assumptions)부터** 정리하세요. 아래 질문들에 대해 당신의 결정을 말해주면 됩니다.

1. out-of-order 허용 범위(지연 도착 최대 몇 초)를 어떻게 둘까요? (예: `lateness L`를 두고 그 이상은 버림)
2. `topk()`는 **정확**이어야 하나요, 아니면 **근사** 허용인가요? (서비스 맥락을 가정해서 선택)
3. eviction 정책은 무엇을 쓰겠습니까? (LRU? LFU? “최근 query 기준” vs “최근 ingest 기준”)
4. 시간 윈도우 (t-W, t] 경계 포함/제외를 어떻게 할까요?
5. `query()` 호출이 없는 유저도 eviction/ttl 대상에서 관리해야 하나요?

가정들을 말한 뒤에, **단어로 high-level design**(자료구조/상태/업데이트 흐름)을 설명해 주세요. 그러고 나서 코딩으로 들어갑니다.

"""


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
