"""
있습니다. 🙂
그리고 **꽤 많이 다릅니다.**
지금 당신이 “window / time” 유형에 이미 포화가 온 상태라서, **축을 바꿔주는 게 맞아요.**

아래는 **시간 슬라이딩과 거의 겹치지 않는**,
하지만 **ML / DL Architect 인터뷰에서 실제로 나오는** 유형입니다.

---

# 새로운 문제 유형

## 🔹 Online Deduplication + Versioned State (시간 아님)

### 문제: 온라인 이벤트 중복 제거 + 최신 상태 유지

당신은 **온라인 ML feature pipeline**을 운영 중입니다.

이벤트 스트림은 다음과 같은 형태로 들어옵니다:

```
(event_id: str, user_id: str, version: int, payload: Any)
```

### 의미

* 같은 `event_id`는 **중복으로 여러 번** 들어올 수 있음
* 같은 `user_id`에 대해 **여러 버전의 상태 업데이트**가 들어올 수 있음
* **항상 최신 version만 유효**
* 이벤트는 **순서 보장 없음** (out-of-order 가능)

---

## 요구사항

1. **중복 이벤트 제거**

   * 같은 `event_id`는 한 번만 처리
2. **user별 최신 상태 유지**

   * `version`이 가장 큰 payload만 유지
3. **메모리 제한**

   * 수백만 이벤트 가능
   * 오래된 `event_id`는 정리 필요
4. **Latency**

   * 이벤트당 O(1) ~ amortized O(1)

---

## API

```python
class StateStore:
    def ingest(self, event_id: str, user_id: str, version: int, payload) -> None:
        ...

    def get_state(self, user_id: str):
        # 해당 user의 최신 payload 반환
```

---

## 일부러 안 준 정보 (당신이 물어봐야 할 것)

* event_id는 **얼마나 오래 기억해야 하나?**
* version은 **항상 증가하나?**
* 동일 version이 다시 들어오면?
* payload 크기는?
* 중복 제거 정확도는 100% 필요한가?

---

## 이 문제의 포인트 (window랑 다름)

이 문제는:

* ❌ 시간 슬라이딩 아님
* ❌ token / rate limiting 아님
* ✅ **idempotency**
* ✅ **state versioning**
* ✅ **out-of-order handling**
* ✅ **memory vs correctness trade-off**

---

## 왜 이게 ML / DL Architect 문제냐

* feature pipeline 중복 제거
* Kafka / streaming ingestion
* online/offline feature store 정합성
* exactly-once vs at-least-once 처리

이건 **모델 문제가 아니라 “데이터가 더러울 때 시스템을 어떻게 설계하느냐”**를 봅니다.

---

## 지금 단계 (아직 코딩 ❌)

이번에도 **코드 쓰지 말고**, 딱 이것만 답해보세요:

1. 이 문제의 **핵심 추상화는 뭐라고 부를 수 있을까요?**
   (힌트: cache, set, map, log…)
2. 중복 제거를 **완벽하게** 하면 어떤 비용이 생길까요?
3. 이걸 **근사**로 바꾸면 어떤 선택지가 있을까요?

이 문제는 **window 감각이 전혀 필요 없습니다.**
그리고 지금 당신 상태에서 **뇌에 아주 좋은 스트레칭**이 될 겁니다.

원하면 다음으로는:

* 큐/백프레셔 문제
* consistency vs availability 문제
* online aggregation without time
* top-k without window

중에서 골라서 갈 수도 있어요.

"""

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
