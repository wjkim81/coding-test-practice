import heapq

class ExpiringCache:
    def __init__(self):
        self.cache = {} # key -> (value, timestamp)
        self.heap = []  

    def set(self, key: str, value: str, timestamp: int, ttl: int) -> None:
        """
        key에 value를 저장한다.
        이 항목은 timestamp + ttl 이후에 만료된다.
        같은 key로 다시 set하면 덮어쓴다.
        """
        expire_time = timestamp + ttl
        self.cache[key] = (value, expire_time)
        heapq.heappush(self.heap, (expire_time, key))
        # cleanup?

    def get(self, key: str, timestamp: int) -> str | None:
        """
        key가 존재하고 만료되지 않았으면 value 반환.
        만료되었거나 없으면 None 반환.
        """
        if key not in self.cache:
            return None
        value, expire_timestamp = self.cache[key]
        if expire_timestamp <= timestamp:
            del self.cache[key] # remove not to be searched
            return None

        return value

    def cleanup(self, timestamp: int) -> int:
        """
        현재 시점에서 만료된 항목을 모두 제거한다.
        제거된 항목 수를 반환한다.
        """
        count = 0
        while self.heap and self.heap[0][0] <= timestamp:
            expire_time, key = heapq.heappop(self.heap)
            if key in self.cache and self.cache[key][1] == expire_time:
                count += 1
                del self.cache[key]

        return count