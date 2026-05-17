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
    