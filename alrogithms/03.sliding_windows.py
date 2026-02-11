"""
좋습니다. 바로 **Problem 3 (Medium)** 갑니다.
이건 코테에서 “Easy 2개 + Medium 1개” 조합일 때 **딱 그 Medium 역할**로 자주 나옵니다.

---

## Day 1 – Problem 3 (Medium)

### Longest Substring Without Repeating Characters (Sliding Window)

#### 문제

문자열 `s`가 주어질 때, **중복 문자가 없는 가장 긴 부분문자열(substring)**의 길이를 반환하라.

* substring = 연속 구간
* 문자 종류는 ASCII라고 가정해도 되고, 일반 문자열로 처리해도 됨

#### 예시

```
s = "abcabcbb"  -> 3   ("abc")
s = "bbbbb"     -> 1   ("b")
s = "pwwkew"    -> 3   ("wke")
s = ""          -> 0
```

---

## 코테에서 보는 포인트

* O(n^2)로 모든 substring 검사하면 감점
* **슬라이딩 윈도우 + last seen index**로 O(n)
* edge case: 반복이 연속/비연속으로 섞일 때 (`abba` 같은 케이스)

---

## 힌트 (원하면 안 보고 풀어도 됨)

* 포인터 두 개: `left`, `right`
* 해시맵: `last_seen[char] = index`
* 만약 `char`가 이미 등장했고 그 index가 `left` 이상이면
  → `left`를 그 다음으로 점프

핵심 한 줄:

* `left = max(left, last_seen[c] + 1)`

---

## 요구사항

* Python 함수:

```python
def length_of_longest_substring(s: str) -> int:
    ...
```

* 시간복잡도 목표: **O(n)**

---

자, 이번에도 **본인 코드 먼저** 붙여주세요.
코드 보고 “설명 문장(면접용)”까지 바로 다듬어 드리겠습니다.

"""

def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0

    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1

        last_seen[c] = right
        best = max(best, right - left + 1)

    return best


# ChatGPT 정답
# def length_of_longest_substring(s: str) -> int:
#     last_seen = {}
#     left = 0
#     best = 0

#     for right, c in enumerate(s):
#         if c in last_seen and last_seen[c] >= left:
#             left = last_seen[c] + 1

#         last_seen[c] = right
#         best = max(best, right - left + 1)
    
#     return best

# 내 정답 버젼
# def length_of_longest_substring(s: str) -> int:
#     seen = {}
#     left = 0
#     longest = 0

#     for right, c in enumerate(s):
#         if c in seen and seen[c] >= left:
#             left = seen[c] + 1

#         seen[c] = right
#         curr_len = right - left + 1
#         if curr_len > longest:
#             longest = curr_len

#     return longest


if __name__ == "__main__":
    s = "abcabcbb" 
    print(length_of_longest_substring(s))
