"""
## 문제: Real-Time Anomaly Rate Monitor

당신은 대규모 API 게이트웨이의 모니터링 시스템을 설계하고 있습니다.

이벤트 스트림이 다음 형태로 들어옵니다:

```
(timestamp: int, endpoint: str, status_code: int)
```

두 가지 기능을 구현해야 합니다:

1. **`record(timestamp, endpoint, status_code)`** — 이벤트를 기록합니다.

2. **`get_error_rate(timestamp, endpoint)`** — 해당 endpoint에 대해 최근 `W`초 동안의 **에러율** (status_code >= 400인 비율)을 반환합니다. 요청이 0건이면 `0.0`을 반환합니다.

추가 맥락 (의도적으로 불완전):
- 수만 개의 endpoint가 존재
- 초당 수십만 건의 이벤트
- `W`는 초기화 시 주어짐
- timestamp는 호출 간 단조 증가한다고 가정해도 됨

---

시작하기 전에, 이 문제에서 **불명확하다고 느끼는 부분**이나 **명시하고 싶은 가정**이 있으면 먼저 말씀해주세요.
"""
from collections import defaultdict, deque
from typing import Optional

class AnomalyRateMonitor:
    def __init__(self, W: int, threshold: float):
        self.W = W
        self.threshold = threshold
        self.records = defaultdict(deque)  # endpoint -> deque of (timestamp, status_code)
        self.error_counts = defaultdict(int)  # endpoint -> count of errors
        self.pushed = defaultdict(bool)  # endpoint -> whether alert has been pushed

    def _prune(self, endpoint: str, curr_time: int) -> None:
        endpoint_q = self.records[endpoint]
        cutoff = curr_time - self.W
        while endpoint_q and endpoint_q[0][0] <= cutoff:
            if endpoint_q[0][1] >= 400:
                self.error_counts[endpoint] -= 1
            endpoint_q.popleft()

    def record(self, timestamp: int, endpoint: str, status_code: int) -> Optional[str]:
        endpoint_q = self.records[endpoint]
        endpoint_q.append((timestamp, status_code))
        if status_code >= 400:
            self.error_counts[endpoint] += 1

        self._prune(endpoint, timestamp)

        error_rate = self.error_counts[endpoint] / len(endpoint_q)

        if error_rate > self.threshold and not self.pushed[endpoint]:
            self.pushed[endpoint] = True
            return endpoint
        elif error_rate < self.threshold and self.pushed[endpoint]:
            self.pushed[endpoint] = False

        return None

    def get_error_rate(self, timestamp: int, endpoint: str) -> float:
        endpoint_q = self.records[endpoint]

        self._prune(endpoint, timestamp)
        

        total = len(endpoint_q)
        if total == 0:
            return 0.0

        error_count = self.error_counts[endpoint]
        return error_count / total

