"""
## 문제: Top-K Frequent Events Tracker

당신은 실시간 검색 시스템의 **인기 검색어 트래커**를 설계하고 있습니다.

이벤트 스트림:

```
(timestamp: int, query: str)
```

구현할 것:

```python
class TopKTracker:
    def __init__(self, W: int, K: int):
        pass

    def record(self, timestamp: int, query: str) -> None:
        # 검색 이벤트를 기록한다
        pass

    def get_top_k(self, timestamp: int) -> list[tuple[str, int]]:
        # 최근 W초 동안 가장 많이 검색된 상위 K개를 반환한다.
        # [(query, count), ...] 형태, count 내림차순.
        # K개 미만이면 있는 만큼만 반환.
        pass
```

---

### 예시

```
W = 10, K = 2

record(1, "chatgpt")
record(2, "chatgpt")
record(3, "gemini")
record(4, "chatgpt")
record(5, "gemini")
record(6, "claude")

get_top_k(6) → [("chatgpt", 3), ("gemini", 2)]

get_top_k(15) → [("claude", 1)]
  # t=1~5 이벤트는 윈도우 밖으로 빠짐
```

---

### 제약 조건
- 수만 종류의 query
- 초당 수십만 건의 이벤트
- `get_top_k()`가 빈번하게 호출됨
- timestamp는 단조 증가

---

### 이전 문제들과 다른 점

- 단순 카운트가 아니라 **정렬이 필요**
- sliding window + **어떤 자료구조를 조합**할 건지가 핵심

---

가정이나 질문부터 시작하세요!
"""