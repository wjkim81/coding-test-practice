import heapq

class TelemetryBuffer:
    def __init__(self, max_size_bytes: int):
        self.max_size = max_size_bytes
        self.heap = []   # (priority, timestamp, event_id, size, data)
        self.current_size = 0
    
    def add_event(
        self, 
        event_id: str,
        priority: int,        # 0=low, 1=medium, 2=high, 3=critical
        size_bytes: int,
        timestamp_ms: float,
        data: dict
    ) -> bool:
        # 1. 새 event 자체 너무 큼? Reject.
        # 2. 공간 충분? 그냥 push.
        # 3. 부족하면 evict 시도:
        #    - Heap top priority < 새 event priority면 pop
        #    - 충분 공간 확보될 때까지 반복
        #    - 도중 더 못 evict면 rollback + reject
        # 4. 성공하면 새 event push.
        # return
        #    True when event is added
        #    False when event is not added

        # Quick reject: event itself larger than max
        if size_bytes > self.max_size:
            return False
        popped = []
        while (
            self.current_size + size_bytes > self.max_size and
            self.heap and
            self.heap[0][0] < priority
        ):
            item = heapq.heappop(self.heap)
            popped.append(item)
            self.current_size -= item[3]

        if self.current_size + size_bytes <= self.max_size:
            heapq.heappush(
                self.heap,
                (priority, timestamp_ms, event_id, size_bytes, data)
            )
            self.current_size += size_bytes
            return True
        
        # rollback
        for item in popped:
            heapq.heappush(self.heap, item)
            self.current_size += item[3]   # ← rollback도 size 복구
        return False
    
    def flush(self) -> list[dict]:
        # 모든 event를 (priority DESC, timestamp ASC)로 sort해서 반환
        # Buffer clear
        sorted_events = sorted(self.heap, key=lambda x: (-x[0], x[1]))

        result = [
            {
                "event_id": event_id,
                "priority": priority,
                "timestamp_ms": ts,
                "size_bytes": size,
                "data": data,
            }
            for priority, ts, event_id, size, data in sorted_events
        ]
        self.heap = []
        self.current_size = 0

        return result