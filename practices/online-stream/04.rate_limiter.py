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

        