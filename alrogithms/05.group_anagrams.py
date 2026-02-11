"""
응 맞아 👍
**지금까지 흐름 기준으로 보면 Day 4가 안 한 게 맞고**, 순서대로 가는 것도 아주 좋은 선택이야.

그럼 이렇게 정리하자.

---

## 지금까지 한 것 정리 (빠르게 체크)

### Day 1–3에서 이미 처리된 것

* ✅ Two Sum
* ✅ Valid Parentheses
* ✅ Longest Substring (개념 이해까지 완료)
* ✅ Product of Array Except Self

이걸로 **hash / stack / sliding window / prefix 사고**는 한 바퀴 돌았어.

---

## 그래서 다음은 👉 **Day 4**

### Day 4 – 패턴: Hashing / Counting

오늘은 **생각보다 연구랑 더 비슷한 날**이야.
(빈도, 분포, grouping → EEG feature aggregation이랑도 닮음)

---

## Day 4 – Problem 1

### Group Anagrams (Medium)

#### 문제

문자열 배열 `strs`가 주어질 때,
**서로 애너그램(anagram)인 문자열끼리 그룹화**해서 반환하라.

* 순서는 상관 없음

#### 예시

```
Input: ["eat","tea","tan","ate","nat","bat"]

Output:
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]
```

---

## 코테에서 보는 핵심 포인트

* “애너그램을 어떻게 같은 그룹으로 판단할 것인가?”
* 정렬 vs 카운팅
* key를 어떻게 만들 것인가?

---

## 힌트 (안 봐도 되지만, 방향만)

애너그램의 본질은:

* **문자 빈도 분포가 동일**

그래서 key 후보는:

1. 문자열 정렬한 결과

   * `"eat"` → `"aet"`
2. 26개 문자 카운트 튜플

   * `(1,0,0,...,1,...)`

둘 다 가능.
👉 **정렬 버전이 구현 가장 쉬움**

---

## 요구사항

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
    ...
```

---

## 진행 방식 (이제 익숙하죠 😄)

1. **코드 먼저 작성**
2. 여기 붙여넣기
3. 내가:

   * key 설계 리뷰
   * 시간/공간 복잡도
   * “왜 이게 맞는지” 면접용 설명 문장 정리

---

이 문제는:

* 문자열이긴 한데
* sliding window ❌
* 상태 점프 ❌
* 그냥 **분포 묶기 문제**

그래서 아까처럼 머리 아프지 않을 거야.

👉 **바로 코드 고고**
(정렬 버전으로 가도 되고, 카운트 버전 도전해도 좋고)

"""

# ChatGPT 정답
from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    def make_key(word: str) -> str:
        return "".join(sorted(word))
    
    groups = defaultdict(list)

    for word in strs:
        key = make_key(word)

        groups[key].append(word)

    return list(groups.values())
        

# def group_anagrams(strs: list[str]) -> list[list[str]]:
#     def make_key(word: str) -> str:
#         return "".join(sorted(word))
    
#     groups = {}
#     for s in strs:
#         key = make_key(s)

#         if key in groups:
#             groups[key].append(s)
#         else:
#             groups[key] = [s]

#     out = list(groups.values())
#     return out

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    groups = group_anagrams(strs)
    print(groups)