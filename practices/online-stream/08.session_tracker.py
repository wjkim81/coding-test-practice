"""
좋아요! 복습용으로 하나 드립니다.

---

## 문제: Per-User Session Tracker

온라인 게임 서버에서 유저별 접속 상태를 모니터링합니다.

이벤트 스트림:

```
(timestamp: int, user_id: str, action: str)
```

`action`은 `"login"` 또는 `"logout"` 중 하나입니다.

구현할 것:

```python
class SessionTracker:
    def __init__(self, W: int):
        pass

    def record(self, timestamp: int, user_id: str, action: str) -> None:
        # 이벤트를 기록한다
        pass

    def get_active_ratio(self, timestamp: int, user_id: str) -> float:
        # 최근 W초 동안 해당 유저의 login 비율을 반환한다.
           이벤트가 0건이면 0.0
        pass
```

---

### 제약 조건
- 수만 명의 유저
- timestamp는 단조 증가
- W는 초기화 시 주어짐

---

어제 풀었던 구조를 떠올리면서 혼자 풀어보세요. 다 풀면 보여주세요!
"""
from collections import defaultdict, deque

class SessionTracker:
    def __init__(self, W: int):
        self.W = W
        self.users = defaultdict(deque) # user_id -> (timestamp, action)
        # why login_counts? it avoids loop iteration to calculate ratio, but we can directly get number of login with space O(1) * (number of users)
        self.login_counts = defaultdict(int)      # user_id -> count (default = 0), count only login
       
    def _prune(self, user_id: str, now: int) -> None:
        user_q = self.users[user_id]
        cutoff = now - self.W

        # if now = 10, W = 5, and event_time = 6: no prune
        # if now = 10, W = 5, and event_time = 4: prune
        # => event_time <= now - W -> prune  , ask whether equal include or not, here I assume include
        # when prune, login_count -= login_count        
        while user_q and user_q[0][0] <= cutoff:
            if user_q[0][1] == 'login':
                self.login_counts[user_id] -= 1
            user_q.popleft()

            
    
    def record(self, timestamp: int, user_id: str, action: str) -> None:
        self._prune(user_id, timestamp)
        user_q = self.users[user_id]
        user_q.append((timestamp, action))
        if action == 'login':
            self.login_counts[user_id] += 1

    def get_active_ratio(self, timestamp: int, user_id: str) -> float:
        # prune here as well to make events sure within window
        self._prune(user_id, timestamp)
        total_events = len( self.users[user_id])
        if total_events == 0: # this is edge case, n_login is also 0, so we need return 0 here
            return 0
        n_logs = self.login_counts[user_id]
        active_ratio = n_logs / total_events
        return active_ratio
    