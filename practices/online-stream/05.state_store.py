import heapq
from typing import Any, Dict, Optional, Tuple

class StateStore:
    def __init__(self, event_ttl: int):
        self.event_ttl = event_ttl

        # event_id dedup with TTL
        self.seen_events = set()                 # event_id membership
        self.expiry_heap = []                    # (expire_time, event_id)

        # user state: user_id -> (version, payload)
        self.user_states: Dict[str, Tuple[int, Any]] = {}

    def _evict_expired_events(self, now: int) -> None:
        while self.expiry_heap and self.expiry_heap[0][0] <= now:
            exp_t, eid = heapq.heappop(self.expiry_heap)
            # Lazy delete: set에 남아있으면 제거
            self.seen_events.discard(eid)

    def _update_state(self, user_id: str, version: int, payload: Any) -> None:
        prev = self.user_states.get(user_id)
        if prev is None or version > prev[0]:
            self.user_states[user_id] = (version, payload)

    def ingest(self, event_time: int, event_id: str, user_id: str, version: int, payload: Any) -> None:
        # TTL-based dedup
        self._evict_expired_events(event_time)

        if event_id in self.seen_events:
            return  # drop duplicate within TTL window

        self.seen_events.add(event_id)
        heapq.heappush(self.expiry_heap, (event_time + self.event_ttl, event_id))

        # Version-based state update (order-independent)
        self._update_state(user_id, version, payload)

    def get_state(self, user_id: str) -> Optional[Any]:
        prev = self.user_states.get(user_id)
        return None if prev is None else prev[1]
