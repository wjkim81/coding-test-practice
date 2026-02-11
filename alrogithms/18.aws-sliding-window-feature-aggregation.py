"""
Problem: Sliding-Window Feature Aggregation for Online ML

- You are building features for an online ML model (fraud detection / recommendations / churn)
- You receive a stream of events in the form: (event_time: int, user_id: str, value: float)
- Specifics:
-    The feature is the sum of values in the last W seconds for that user
-    Ignore events older than current_time - W
-    You may assume:
-        - W is provided at initialization
-        - current_time is non-decreasing across calls

Key Constraints:
- Millions of users
- High event rate
- Low latency


(curr_time: int, event_time: int, user_id: str, value: float)

events acculmulate all even and store is as list of dictionay:
   
events = [
    {event_time: e_t,
     user_id: uid,
     value: v
    }]

left = 0
events = []
def stream(event: dict, user_id: str, curr_time: int) -> float:
    W =

    events.append(event)
    value, left = feature(events, user_id, left, curr_time, W)
   

when we extract feature M times..
my previous approach M * N (N is growing everytime new event comes)

with this feature we can ignore M just scane N, usually scan time n < N


e1, e2, e3, e4, e5, e6
                   | left as start index to search in the loop

def feature(events: list[dict], , user_id: str, left: int, curr_time: int, W: int) -> float:
    start_idx = left
    for i in range(start_idx, len(events)):
        if events[i]["user_id"] == user_id and events[i]["event_time"] <= curr_time - W:
            left = start_idx
            break
       
    sum_value = 0
    for i in range(left, len(events)):
        sum_value += events[i]["value"]
   
   
    return sum_value, left

"""

# ChatGPT Implementation
from collections import deque
from typing import Deque, Dict, Tuple

class SlidingWindowUserSum:
    def __init__(self, W: int):
        self.W = W
        self.q: Dict[str, Deque[Tuple[int, float]]] = {}
        self.s: Dict[str, float] = {}  # running sum per user

    def update(self, curr_time: int, event_time: int, user_id: str, value: float) -> float:
        # Assumption: curr_time is non-decreasing (given).
        # Common additional assumption: events arrive roughly in time order per user.
        if user_id not in self.q:
            self.q[user_id] = deque()
            self.s[user_id] = 0.0

        dq = self.q[user_id]
        self.s[user_id] += value
        dq.append((event_time, value))

        cutoff = curr_time - self.W

        # Evict too-old events (choose < or <= depending on definition)
        while dq and dq[0][0] < cutoff:
            old_t, old_v = dq.popleft()
            self.s[user_id] -= old_v

        return self.s[user_id]

# Claude Implementation
from collections import defaultdict, deque

class SlidingWindowAggregator:
    def __init__(self, W: int):
        self.W = W
        # 각 유저별로 (event_time, value) 저장
        self.user_events = defaultdict(deque)  # user_id -> deque of (time, value)
        self.user_sum = defaultdict(float)     # user_id -> current sum
    
    def add_event(self, curr_time: int, event_time: int, user_id: str, value: float) -> float:
        """
        이벤트 추가하고, 해당 유저의 현재 W-window 합계 반환
        """
        user_q = self.user_events[user_id]
        
        # 1. 새 이벤트 추가
        user_q.append((event_time, value))
        self.user_sum[user_id] += value
        
        # 2. 오래된 이벤트 제거 (curr_time - W 이전 것들)
        cutoff = curr_time - self.W
        while user_q and user_q[0][0] < cutoff:
            old_time, old_value = user_q.popleft()
            self.user_sum[user_id] -= old_value
        
        return self.user_sum[user_id]
    
    def get_feature(self, curr_time: int, user_id: str) -> float:
        """
        이벤트 추가 없이 현재 합계만 조회 (필요시)
        """
        user_q = self.user_events[user_id]
        
        # 오래된 것 제거
        cutoff = curr_time - self.W
        while user_q and user_q[0][0] < cutoff:
            old_time, old_value = user_q.popleft()
            self.user_sum[user_id] -= old_value
        
        return self.user_sum[user_id]
"""

## 복잡도 분석

| 연산 | 복잡도 | 이유 |
|------|--------|------|
| add_event | **O(1) amortized** | 각 이벤트는 한 번 추가, 한 번 제거 |
| 공간 | O(총 active 이벤트 수) | 오래된 건 자동 삭제 |

---

## 핵심 아이디어

❌ 틀린 접근: 전체 이벤트 리스트 + 매번 user 필터링
✅ 맞는 접근: user별 deque + running sum 유지
"""