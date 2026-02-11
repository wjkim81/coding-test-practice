"""
## Day 9-2️⃣ Minimum Window Substring

**(Sliding Window, Medium–Hard 경계)**

⚠️ 이 문제는 **완벽 구현이 목표가 아닙니다.**
👉 **사고 구조를 이해하는 게 목표**

---

### 문제 요약

문자열 `s`와 `t`가 주어질 때,
`t`의 모든 문자를 포함하는 **가장 짧은 substring**을 반환하라.

---

### 핵심 관찰

* substring → 연속
* shortest → **확장 + 수축**
* 문자의 “개수” 중요 → hashmap 필요

👉 **정형화된 sliding window 문제**

---

### 사고 흐름 (이걸 외우세요)

1. `need`: t의 문자 빈도
2. `have`: 현재 window의 문자 빈도
3. `formed`: 조건 만족한 문자 개수
4. right 포인터 확장 → 조건 만족할 때까지
5. 조건 만족하면 left 포인터 수축 → 최소 길이 갱신

---

### 코드 (표준, 하지만 길어서 “읽기용”)

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0

    l = 0
    ans = (float('inf'), None, None)

    for r, c in enumerate(s):
        have[c] = have.get(c, 0) + 1

        if c in need and have[c] == need[c]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            left_char = s[l]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            l += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

---

### 이 문제의 “진짜 포인트”

* sliding window는 **조건을 만족할 때만 줄인다**
* 조건이 깨지면 다시 확장
* **확장/수축의 책임 분리**

---

### 면접에서 솔직한 한 문장 (시니어 톤)

> “This is a classic sliding window problem. I track required character counts and shrink the window only when all constraints are satisfied.”

이 정도면 충분합니다.

---

## Day 9 마무리 체크리스트

오늘 끝나면 아래가 말로 바로 나오면 성공입니다:

* “왜 prefix sum + hashmap이 필요한지”
* “왜 sliding window는 음수 있으면 안 되는지”
* “Minimum window에서 formed/required의 역할”

---

## 지금 상황에 대한 정확한 평가

* Day 1–8: **패턴 습득**
* **Day 9: 패턴을 말로 설명 가능해짐**
* 이제 코테는 **더 이상 늘리지 않아도 되는 상태**

---

다음 선택지만 남았습니다:

1️⃣ **Day 9 문제 중 하나를 직접 다시 써볼까?**
2️⃣ **Day 1–9 전체 코테 패턴 1페이지 요약**
3️⃣ **ML/Research 인터뷰 대비: “이 알고리즘을 연구에 어떻게 연결해서 말할지”**

지금 가장 필요한 걸로 바로 이어갈게요.

"""

from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0

    l = 0
    ans = (float('inf'), None, None)

    for r, c in enumerate(s):
        have[c] = have.get(c, 0) + 1

        if c in need and have[c] == need[c]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            left_char = s[l]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            l += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


if __name__ == "__main__":
    s = "AAABBC"
    t = "AABC"
    print(min_window(s, t))
