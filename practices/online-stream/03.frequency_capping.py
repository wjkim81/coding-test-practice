from collections import defaultdict, deque
import bisect

class FeatureStore:
    def __init__(self, window_size: int):
        self.window_size = window_size
        # (user_id, ad_id) -> deque of (timestamps, value)
        self.records = defaultdict(deque)
        self.time_exposed = defaultdict(int)  # (user_id, ad_id) -> current exposed time to ads

    def _prune(self, key: tuple, curr_time: int) -> None:
        record_q = self.records[key]
        cutoff = curr_time - self.window_size
        while record_q and record_q[0][0] < cutoff:
            old_time, old_value = record_q.popleft()
            self.time_exposed[key] -= old_value



    def record_event(self, timestamp: int, user_id: str, ad_id: str, value: float) -> None:
        key = (user_id, ad_id)
        record_q = self.records[key]
        
        # 1. Out-of-order 처리: 끝의 몇 개만 뒤집힌 경우가 대부분임
        if not record_q or timestamp >= record_q[-1][0]:
            record_q.append((timestamp, value))
        else:
            # 드문 경우에만 bisect로 위치 찾아 삽입 (O(N) in deque, but usually small N)
            # deque은 중간 삽입이 비효율적이므로 실무에선 list + bisect를 고민하기도 함
            bisect.insort(record_q, (timestamp, value))
        
        self.time_exposed[key] += value
        self._prune(key, timestamp)


    def get_feature(self, current_time: int, user_id: str, ad_id: str) -> float:
        key = (user_id, ad_id)
        self._prune(key, current_time)

        return self.time_exposed[(user_id, ad_id)]