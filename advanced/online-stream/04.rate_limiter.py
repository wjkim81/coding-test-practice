"""
좋습니다. **완전히 다른 축의 문제**로 가겠습니다.
난이도는 *medium–hard*, 하지만 이번엔 **집계가 아니라 “제어(control)” 문제**입니다.
(역시 코테 패턴 냄새는 최대한 제거)

---

# 문제: 시간 기반 Adaptive Rate Limiter (온라인 ML / API 서빙 맥락)

당신은 **온라인 ML 추론 API**(LLM / 추천 / 랭킹 등)를 운영 중입니다.
요청은 API key(또는 user_id) 단위로 들어오며, **시간에 따라 제한을 걸어야** 합니다.

---

## 입력 스트림

각 요청은 다음 형태로 들어옵니다.

```
(request_time: int, api_key: str, cost: int)
```

* `request_time`: 초 단위 타임스탬프 (non-decreasing 보장)
* `api_key`: 사용자 또는 고객 키
* `cost`: 요청의 비용

  * 예: 간단한 모델 = 1
  * 큰 LLM 추론 = 10

---

## 요구사항 (의도적으로 덜 명확)

각 `api_key`에 대해 다음 규칙을 만족해야 합니다.

### 기본 제한

* **슬라이딩 윈도우 W초** 동안
* 누적 `cost`의 합이 **LIMIT**을 넘으면 요청을 **거절**

### 추가 트위스트 (중요)

1. **Burst 허용**

   * 짧은 시간에 몰리는 요청은 어느 정도 허용해야 함
2. **Idle 크레딧**

   * 오래 쉬던 key는 잠깐 더 쓸 수 있어도 됨
3. **메모리 제한**

   * 수백만 key 가능
   * 오래 안 쓰는 key는 정리 필요
4. **Latency**

   * 요청당 O(1) ~ amortized O(1) 기대

---

## API

아래 클래스를 설계/구현한다고 가정합니다.

```python
class RateLimiter:
    def __init__(self, W: int, limit: int, ttl: int):
        ...

    def allow(self, request_time: int, api_key: str, cost: int) -> bool:
        # 허용되면 True, 거절되면 False
```

---

## 명시되지 않은 부분 (당신이 정해야 함)

이 문제는 **가정 능력**을 봅니다.
코딩 전에 반드시 정해야 할 질문들:

1. Burst는 **얼마나** 허용할 것인가?

   * 고정 버퍼?
   * idle 시간에 비례?
2. Sliding window는

   * 정확 window?
   * 근사(windowed counter)?
3. idle 크레딧은

   * 상한이 있는가?
   * 무한 누적 가능한가?
4. TTL은

   * 마지막 request 기준?
   * allow 호출 기준?
5. 거절된 요청은

   * state에 반영하는가?
   * 완전히 무시하는가?

---

## 지금 단계 (중요)

아직 **코드 쓰지 마세요.**

### 당신 차례:

아래를 **말로만** 정리해 주세요.

1. 이 문제를 어떤 **고전 개념**으로 환원할 수 있을까요?
   (힌트: sliding window 말고도 있음)
2. Burst + idle 크레딧을 동시에 만족하려면
   **어떤 상태(state)** 를 api_key마다 들고 있어야 할까요?
3. 이게 **왜 ML/DL Solution Architect 문제**인지 한 문장으로 설명해 보세요.

이거 정리되면, 그 다음에야 설계 → 코드로 들어갑니다.

"""

from typing import Dict, Tuple

class RateLimiter:
    """
    Token Bucket rate limiter.

    - refill_rate = limit / W  (tokens per second)
    - max_tokens: burst cap (default = limit)
    - allow(t, key, cost): if enough tokens, deduct and allow
    - request_time is assumed non-decreasing globally (interview-friendly assumption)
    """

    def __init__(self, W: int, limit: int, ttl: int, max_tokens: int | None = None):
        self.W = W
        self.limit = limit
        self.ttl = ttl  # optional: memory cleanup only
        self.refill_rate = limit / W

        self.max_tokens = max_tokens if max_tokens is not None else float(limit)

        # api_key -> (tokens, last_time)
        self.state: Dict[str, Tuple[float, int]] = {}

        # api_key -> last_seen_time (for TTL cleanup)
        self.last_seen: Dict[str, int] = {}

    def _evict_if_expired(self, now: int, api_key: str) -> None:
        """Lazy TTL eviction: remove inactive keys to control memory."""
        if self.ttl <= 0:
            return
        last = self.last_seen.get(api_key)
        if last is not None and (now - last) > self.ttl:
            self.state.pop(api_key, None)
            self.last_seen.pop(api_key, None)

    def allow(self, request_time: int, api_key: str, cost: int) -> bool:
        # TTL cleanup (optional)
        self._evict_if_expired(request_time, api_key)

        # Load state (initialize with full bucket)
        tokens, last_time = self.state.get(api_key, (self.max_tokens, request_time))

        # Refill tokens based on elapsed time
        elapsed = request_time - last_time
        if elapsed > 0:
            tokens = min(self.max_tokens, tokens + elapsed * self.refill_rate)

        # Decide
        if tokens < cost:
            # update last_seen even if rejected? (policy choice)
            # 보통은 DoS 방어 관점에서 "거절도 last_seen 갱신"을 하기도 함.
            # 여기서는 간단히 갱신하겠습니다.
            self.last_seen[api_key] = request_time
            self.state[api_key] = (tokens, request_time)
            return False

        # Accept: deduct cost and store updated state
        tokens -= cost
        self.state[api_key] = (tokens, request_time)
        self.last_seen[api_key] = request_time
        return True

        