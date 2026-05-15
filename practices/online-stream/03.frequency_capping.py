"""
## 💻 인터뷰 문제: 대규모 광고 시스템의 실시간 빈도 제한(Frequency Capping) 모니터링

당신은 글로벌 광고 서빙 플랫폼의 아키텍트입니다. 특정 광고(ad_id)가 단기간에 특정 사용자(user_id)에게 너무 많이 노출되는 것을 방지하기 위해, **"최근 시간 동안 발생한 사용자별 광고 노출 횟수"**를 실시간으로 집계하는 시스템을 설계해야 합니다.

이 데이터는 후속 모델의 피처로 입력되거나, 서빙 엔진에서 즉시 필터링 용도로 사용됩니다.

### **상황 설명**

* **입력 데이터:** `(timestamp: int, user_id: str, ad_id: str)` 형태의 스트림이 들어옵니다.
* **요구사항:** 특정 `user_id`와 `ad_id`가 주어졌을 때, 현재 시점()을 기준으로 최근 초 동안 해당 광고가 몇 번 노출되었는지 반환하는 함수를 구현하세요.
* **제약 조건:**
1. **메모리 효율성:** 사용자가 수억 명이고 광고 종류도 방대합니다. 모든 데이터를 무기한 저장할 수 없으며, 윈도우()를 벗어난 데이터는 즉시 혹은 효율적으로 **삭제(Eviction)**되어야 합니다.
2. **지연 시간(Latency):** 집계 결과는 밀리초(ms) 단위 내에 반환되어야 합니다.
3. **데이터 특성:** 이벤트의 `timestamp`는 대체로 증가하는 순서로 들어오지만, 아주 가끔 네트워크 지연으로 인해 **약간의 순서 뒤바뀜(Out-of-order, 최대 1~2초)**이 발생할 수 있습니다.



---

### **진행 순서**

1. **가정 사항 확인:** 설계를 시작하기 전, 문제에서 모호한 부분이나 시스템 한계에 대해 저에게 질문해 주세요.
2. **고수준 설계:** 어떤 자료구조를 쓸 것인지, 메모리 관리는 어떻게 할 것인지 말로 설명해 주세요.
3. **코드 구현:** 설계가 합의되면 코드를 작성합니다.

먼저, 어떤 부분들을 확인하고 싶으신가요? 질문부터 시작해 주십시오.
"""

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