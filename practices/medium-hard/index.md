

---

# 코딩 면접 연습 — Medium~Hard 문제 정리

## 전체 패턴 맵

| 자료구조 조합 | 문제 |
|-------------|------|
| deque + running counter + prune | AnomalyMonitor, SessionTracker, TopKTracker |
| deque만 | RateLimiter |
| HashMap + Doubly Linked List | LRU Cache |
| HashMap + Heap (lazy deletion) | ExpiringCache |
| reverse map + in_degree + BFS queue | 위상 정렬 (TaskScheduler) |
| deque + sorted list (bisect) | MovingMedian |
| nested defaultdict + 첫 이벤트 추적 | NotificationAggregator |
| Dual Heap + 상태 전이 | TaskExecutor |
| deque + counter + 동적 서버 관리 | LoadBalancer |

---

## 문제 1: Sliding-Window Anomaly Rate Monitor

### 유형: Streaming + Sliding Window + Per-Key State
### 난이도: Medium

**문제:** API 엔드포인트별로 최근 W초 동안의 에러율(status_code >= 400)을 실시간 추적.
threshold 초과 시 알림 (중복 방지 + 재알림).

**핵심 자료구조:** `defaultdict(deque)` + `defaultdict(int)` + `defaultdict(bool)`

**배운 것:**
- per-key deque로 윈도우 관리
- running counter로 O(1) 집계 (매번 순회 X)
- lazy eviction (_prune 패턴)
- edge-triggered alert (pushed flag)

```python
from collections import defaultdict, deque
from typing import Optional

class AnomalyRateMonitor:
    def __init__(self, W: int, threshold: float):
        self.W = W
        self.threshold = threshold
        self.records = defaultdict(deque)
        self.error_counts = defaultdict(int)
        self.pushed = defaultdict(bool)

    def _prune(self, endpoint: str, curr_time: int) -> None:
        endpoint_q = self.records[endpoint]
        cutoff = curr_time - self.W
        while endpoint_q and endpoint_q[0][0] <= cutoff:
            if endpoint_q[0][1] >= 400:
                self.error_counts[endpoint] -= 1
            endpoint_q.popleft()

    def record(self, timestamp: int, endpoint: str, status_code: int) -> Optional[str]:
        endpoint_q = self.records[endpoint]
        endpoint_q.append((timestamp, status_code))
        if status_code >= 400:
            self.error_counts[endpoint] += 1
        self._prune(endpoint, timestamp)
        error_rate = self.error_counts[endpoint] / len(endpoint_q)
        if error_rate > self.threshold and not self.pushed[endpoint]:
            self.pushed[endpoint] = True
            return endpoint
        elif error_rate < self.threshold and self.pushed[endpoint]:
            self.pushed[endpoint] = False
        return None

    def get_error_rate(self, timestamp: int, endpoint: str) -> float:
        self._prune(endpoint, timestamp)
        total = len(self.records[endpoint])
        if total == 0:
            return 0.0
        return self.error_counts[endpoint] / total
```

---

## 문제 2: Per-User Session Tracker (복습)

### 유형: Streaming + Sliding Window + Per-Key State
### 난이도: Medium

**문제:** 유저별 최근 W초 동안 login 비율 추적.

**핵심 자료구조:** `defaultdict(deque)` + `defaultdict(int)`

**배운 것:**
- 문제 1과 동일한 뼈대 재활용
- 검사 → 카운터 업데이트 → popleft 순서 중요!

```python
from collections import defaultdict, deque

class SessionTracker:
    def __init__(self, W: int):
        self.W = W
        self.users = defaultdict(deque)
        self.login_counts = defaultdict(int)

    def _prune(self, user_id: str, now: int) -> None:
        user_q = self.users[user_id]
        cutoff = now - self.W
        while user_q and user_q[0][0] <= cutoff:
            if user_q[0][1] == 'login':
                self.login_counts[user_id] -= 1
            user_q.popleft()

    def record(self, timestamp: int, user_id: str, action: str) -> None:
        self._prune(user_id, timestamp)
        self.users[user_id].append((timestamp, action))
        if action == 'login':
            self.login_counts[user_id] += 1

    def get_active_ratio(self, timestamp: int, user_id: str) -> float:
        self._prune(user_id, timestamp)
        total = len(self.users[user_id])
        if total == 0:
            return 0.0
        return self.login_counts[user_id] / total
```

---

## 문제 3: Rate Limiter

### 유형: Streaming + Sliding Window + 판단 (bool)
### 난이도: Medium

**문제:** 클라이언트별로 최근 W초 동안 max_requests 이하인지 판단.

**핵심 자료구조:** `defaultdict(deque)`

**배운 것:**
- running counter 불필요 (len(deque)로 충분)
- 허용된 요청만 기록
- `<` vs `<=` 경계값 주의

```python
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, window: int):
        self.max_requests = max_requests
        self.window = window
        self.client_requests = defaultdict(deque)

    def _prune(self, client_id: str, now: int) -> None:
        client_q = self.client_requests[client_id]
        cutoff = now - self.window
        while client_q and client_q[0] <= cutoff:
            client_q.popleft()

    def allow(self, timestamp: int, client_id: str) -> bool:
        self._prune(client_id, timestamp)
        if len(self.client_requests[client_id]) < self.max_requests:
            self.client_requests[client_id].append(timestamp)
            return True
        return False

    def get_remaining(self, timestamp: int, client_id: str) -> int:
        self._prune(client_id, timestamp)
        return self.max_requests - len(self.client_requests[client_id])
```

---

## 문제 4: Dependency-Aware Task Scheduler (위상 정렬)

### 유형: Graph + BFS + Topological Sort
### 난이도: Medium-Hard

**문제:** 의존성을 고려한 태스크 실행 순서 결정. 순환 감지.

**핵심 자료구조:** `defaultdict(list)` (reverse map) + `defaultdict(int)` (in_degree) + `deque` (BFS queue)

**배운 것:**
- 위상 정렬 5줄 템플릿
- reverse map (누가 나를 기다리나)
- in_degree == 0이면 queue에
- 결과 길이 != 전체 → 순환

```python
from collections import defaultdict, deque

def schedule(tasks: dict[str, list[str]]) -> list[str]:
    reverse = defaultdict(list)
    in_degree = defaultdict(int)
    q = deque()

    for task, deps in tasks.items():
        in_degree[task] = len(deps)
        if len(deps) == 0:
            q.append(task)
        for dep in deps:
            reverse[dep].append(task)

    res_seq = []
    while q:
        task = q.popleft()
        res_seq.append(task)
        for next_task in reverse[task]:
            in_degree[next_task] -= 1
            if in_degree[next_task] == 0:
                q.append(next_task)

    if len(res_seq) != len(tasks):
        return []
    return res_seq
```

---

## 문제 5: Top-K Frequent Events Tracker

### 유형: Streaming + Sliding Window + Heap (Lazy Top-K)
### 난이도: Medium-Hard

**문제:** 실시간 검색어 스트림에서 최근 W초 동안 가장 많이 검색된 상위 K개 반환.

**핵심 자료구조:** `deque` (전체) + `defaultdict(int)` (카운트) + `heapq.nlargest`

**배운 것:**
- heap 실시간 유지 vs lazy approach 트레이드오프
- 전체 deque vs per-key deque 선택
- heap 중간 원소 업데이트 불가 → lazy가 현실적

```python
from collections import defaultdict, deque
import heapq

class TopKTracker:
    def __init__(self, W: int, K: int):
        self.W = W
        self.K = K
        self.events = deque()
        self.counts = defaultdict(int)

    def _prune(self, now: int) -> None:
        cutoff = now - self.W
        while self.events and self.events[0][0] < cutoff:
            _, query = self.events[0]
            self.counts[query] -= 1
            if self.counts[query] == 0:
                del self.counts[query]
            self.events.popleft()

    def record(self, timestamp: int, query: str) -> None:
        self._prune(timestamp)
        self.events.append((timestamp, query))
        self.counts[query] += 1

    def get_top_k(self, timestamp: int) -> list[tuple[str, int]]:
        self._prune(timestamp)
        return heapq.nlargest(self.K, self.counts.items(), key=lambda x: x[1])
```

---

## 문제 6: LRU Cache

### 유형: HashMap + Doubly Linked List
### 난이도: Medium-Hard (Classic)

**문제:** get/put 모두 O(1)인 LRU 캐시. capacity 초과 시 가장 오래 안 쓴 항목 제거.

**핵심 자료구조:** `dict` (HashMap) + Doubly Linked List (dummy head/tail)

**배운 것:**
- HashMap으로 O(1) 조회 + Linked List로 O(1) 순서 관리
- dummy head/tail로 edge case 방지
- helper 분리: _remove, _add_to_front, _move_to_front, _evict_lru

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
        else:
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                self._evict_lru()
```

---

## 문제 7: Expiring Key-Value Store (TTL Cache)

### 유형: HashMap + Heap + Lazy Deletion
### 난이도: Medium-Hard

**문제:** 항목별 개별 TTL이 있는 캐시. cleanup()으로 만료 항목 일괄 제거.

**핵심 자료구조:** `dict` (cache) + `heap` (만료시간순)

**배운 것:**
- 개별 TTL → 삽입 순서 ≠ 만료 순서 → heap 필요
- 좀비 항목 (같은 key 재set) → == 비교로 lazy deletion
- get()에서 개별 만료 체크 + cleanup()에서 일괄 정리

```python
import heapq

class ExpiringCache:
    def __init__(self):
        self.cache = {}
        self.heap = []

    def set(self, key: str, value: str, timestamp: int, ttl: int) -> None:
        expire_time = timestamp + ttl
        self.cache[key] = (value, expire_time)
        heapq.heappush(self.heap, (expire_time, key))

    def get(self, key: str, timestamp: int) -> str | None:
        if key not in self.cache:
            return None
        value, expire_timestamp = self.cache[key]
        if expire_timestamp <= timestamp:
            del self.cache[key]
            return None
        return value

    def cleanup(self, timestamp: int) -> int:
        count = 0
        while self.heap and self.heap[0][0] <= timestamp:
            expire_time, key = heapq.heappop(self.heap)
            if key in self.cache and self.cache[key][1] == expire_time:
                count += 1
                del self.cache[key]
        return count
```

---

## 문제 8: Moving Median Tracker

### 유형: Sliding Window + Sorted List (bisect)
### 난이도: Hard

**문제:** 최근 W초 동안의 센서 값 중앙값을 실시간 추적.

**핵심 자료구조:** `deque` (윈도우) + `sorted list` (bisect.insort)

**배운 것:**
- 정렬 기반 통계 → heap만으로 부족 (중간 삭제 불가)
- 트레이드오프: exact vs approximate median
- bisect.insort: O(log N) 탐색 + O(N) 삽입

```python
import bisect
from collections import deque

class MovingMedian:
    def __init__(self, W: int):
        self.in_windows = deque()
        self.sorted_values = []
        self.W = W

    def _prune(self, now: int) -> None:
        cutoff = now - self.W
        while self.in_windows and self.in_windows[0][0] < cutoff:
            value = self.in_windows[0][1]
            self.sorted_values.remove(value)
            self.in_windows.popleft()

    def add(self, timestamp: int, value: float) -> None:
        self._prune(timestamp)
        self.in_windows.append((timestamp, value))
        bisect.insort(self.sorted_values, value)

    def get_median(self, timestamp: int) -> float | None:
        self._prune(timestamp)
        n = len(self.sorted_values)
        if n == 0:
            return None
        if n % 2 == 1:
            return self.sorted_values[n // 2]
        else:
            return (self.sorted_values[n//2 - 1] + self.sorted_values[n//2]) / 2
```

---

## 문제 9: Event-Driven Notification Aggregator

### 유형: Per-User 집계 + 배치 발송 + 초기화
### 난이도: Medium

**문제:** 유저별 이벤트를 모아서, 첫 이벤트로부터 delay초 후 요약 발송.

**핵심 자료구조:** `defaultdict(lambda: defaultdict(int))` + `dict` (첫 이벤트 시간)

**배운 것:**
- nested defaultdict 문법: `defaultdict(lambda: defaultdict(int))`
- 실시간 카운트 vs lazy 카운트 트레이드오프
- dict 순회 중 삭제 → `list()` 복사본으로 해결

```python
from collections import defaultdict

class NotificationAggregator:
    def __init__(self, delay: int):
        self.delay = delay
        self.users_events = defaultdict(lambda: defaultdict(int))
        self.first_event_time = {}

    def add_event(self, timestamp: int, user_id: str, event_type: str) -> None:
        self.users_events[user_id][event_type] += 1
        if user_id not in self.first_event_time:
            self.first_event_time[user_id] = timestamp

    def get_pending(self, timestamp: int) -> list[tuple[str, dict[str, int]]]:
        ret = []
        for user_id, first_ts in list(self.first_event_time.items()):
            if first_ts + self.delay <= timestamp:
                ret.append((user_id, dict(self.users_events[user_id])))
                del self.users_events[user_id]
                del self.first_event_time[user_id]
        return ret
```

---

## 문제 10: Concurrent Task Executor with Priority

### 유형: Dual Heap + 상태 전이 (running/queued/completed)
### 난이도: Hard

**문제:** 우선순위 기반 작업 큐. 동시 실행 제한. 완료 시 대기열에서 자동 승격.

**핵심 자료구조:** `heap` (running: 완료시간순) + `heap` (queued: 우선순위순) + `list` (completed)

**배운 것:**
- dual heap: 각 heap의 정렬 기준이 다름
- 음수 priority로 max-heap 구현
- _process() 헬퍼로 상태 전이 분리
- submit_order로 동일 우선순위 시 FIFO 보장

```python
import heapq

class TaskExecutor:
    def __init__(self, max_concurrent: int):
        self.max_run = max_concurrent
        self.running = []
        self.queued = []
        self.completed = []

    def _process(self, timestamp: int) -> None:
        while self.running and self.running[0][0] <= timestamp:
            _, task_id = heapq.heappop(self.running)
            self.completed.append(task_id)
        while self.queued and len(self.running) < self.max_run:
            _, _, task_id, duration = heapq.heappop(self.queued)
            heapq.heappush(self.running, (timestamp + duration, task_id))

    def submit(self, timestamp: int, task_id: str, priority: int, duration: int) -> None:
        self._process(timestamp)
        if len(self.running) < self.max_run:
            heapq.heappush(self.running, (timestamp + duration, task_id))
        else:
            heapq.heappush(self.queued, (-priority, timestamp, task_id, duration))

    def get_status(self, timestamp: int) -> dict:
        self._process(timestamp)
        return {
            "running": [r[1] for r in self.running],
            "queued": [q[2] for q in sorted(self.queued)],
            "completed": self.completed
        }
```

---

## 문제 11: Distributed Rate-Aware Load Balancer

### 유형: Sliding Window + 동적 서버 관리 + Lazy Deletion
### 난이도: Hard

**문제:** 여러 서버에 요청 분배. 서버별 capacity와 현재 부하를 고려해 여유율이 가장 높은 서버 선택.

**핵심 자료구조:** `deque` (전체 요청 로그) + `defaultdict(int)` (서버별 카운트) + `dict` (서버 capacity)

**배운 것:**
- 여러 패턴의 조합 (RateLimiter + Priority 선택 + 동적 등록/제거)
- 서버 제거 시 deque에 남은 좀비 → lazy deletion
- 여유율 기반 정렬로 서버 선택

```python
from collections import defaultdict, deque

class LoadBalancer:
    def __init__(self, W: int):
        self.W = W
        self.servers = {}
        self.counts = defaultdict(int)
        self.running_q = deque()

    def _prune(self, curr: int) -> None:
        cutoff = curr - self.W
        while self.running_q and self.running_q[0][0] <= cutoff:
            _, server_id = self.running_q.popleft()
            if server_id in self.counts:
                self.counts[server_id] -= 1

    def register_server(self, server_id: str, capacity: int) -> None:
        self.servers[server_id] = capacity

    def remove_server(self, server_id: str) -> None:
        del self.servers[server_id]
        del self.counts[server_id]

    def route(self, timestamp: int) -> str | None:
        rates = self.get_load(timestamp)
        sorted_rates = sorted(rates.items(), key=lambda x: x[1])
        if not sorted_rates or sorted_rates[0][1] >= 1.0:
            return None
        server_id = sorted_rates[0][0]
        self.counts[server_id] += 1
        self.running_q.append((timestamp, server_id))
        return server_id

    def get_load(self, timestamp: int) -> dict[str, float]:
        self._prune(timestamp)
        rates = {}
        for server, cap in self.servers.items():
            running = self.counts.get(server, 0)
            rates[server] = running / cap
        return rates
```

---

## 핵심 멘탈 모델 요약

### 반복되는 뼈대 패턴:

```
1. _prune(timestamp): 만료된 데이터 정리
2. record/add/submit: 데이터 추가 + prune 호출
3. get_XXX: prune 호출 + 결과 계산/반환
```

### 자주 쓰이는 조합:

```
per-key 상태 관리    → defaultdict(deque) + defaultdict(int)
만료 순서 정렬       → heap (min-heap)
우선순위 처리        → heap (음수로 max-heap)
O(1) 조회 + 순서 관리 → HashMap + Linked List
정렬 상태 유지        → bisect.insort
```

### 반드시 기억할 것:

```
✅ 검사 → 카운터 업데이트 → popleft (절대 popleft 먼저 하지 않는다)
✅ dict 순회 중 삭제 → list() 복사본
✅ heap은 top만 보장 (정렬된 리스트가 아님)
✅ lazy deletion: pop할 때 유효성 확인 (== 비교)
✅ < vs <= 경계값 항상 명시
```
