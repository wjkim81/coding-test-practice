from collections import deque, defaultdict

class VehicleRateLimiter:
    def __init__(self, max_calls_per_minute: int):
        self.max_calls_per_minute = max_calls_per_minute
        self.vehicles = defaultdict(deque)
        self.one_minute = 60_000
    
    def _prune(self, vehicle_id: str, now: float) -> None:
        q = self.vehicles[vehicle_id]
        while q and now - q[0] > self.one_minute:  # ← > 로 수정
            q.popleft()
    
    def allow_request(self, vehicle_id: str, timestamp_ms: float) -> bool:
        # 1. Prune first
        self._prune(vehicle_id, timestamp_ms)
        
        q = self.vehicles[vehicle_id]
        
        # 2. Decision
        if len(q) < self.max_calls_per_minute:
            q.append(timestamp_ms)
            return True
        else:
            return False