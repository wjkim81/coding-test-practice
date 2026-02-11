"""
오늘은 **Day 1 – 문제 1**만 딱 깔끔하게 시작하죠.

---

## Day 1 – Coding Test

### Problem 1: Two Sum (Easy, but “생각을 본다” 문제)

#### 문제

정수 배열 `nums`와 정수 `target`이 주어질 때,
두 수를 더해서 `target`이 되는 **서로 다른 인덱스 두 개**를 반환하라.

* 각 입력에는 **정확히 하나의 해답**이 있다고 가정
* 같은 원소를 두 번 사용할 수 없음
* 반환 순서는 상관없음

#### 예시

```
nums = [2, 7, 11, 15], target = 9
→ [0, 1]
```

---

## 요구사항 (코테 기준)

* 시간복잡도: **O(n)** 기대
* Python
* 라이브러리 사용 자유 (`dict` 허용)
* edge case 고려 (음수, 중복값)

---

## 진행 방식

1. **본인 코드 먼저 작성** (주석 최소, 실전처럼)
2. 여기 그대로 붙여넣기
3. 내가 다음 관점에서 리뷰

   * 알고리즘 선택 이유
   * 시간/공간 복잡도
   * 인터뷰에서 말하기 좋은 설명 문장
   * “너무 정답처럼 보이지 않게” 다듬기

---

### 힌트 (원하면 안 보고 풀어도 됨)

* 한 번의 loop 안에서 해결 가능
* “이미 봤던 값”을 어떻게 기억할지 생각

---

자, **코드부터 던져주세요.**
사람이 푼 티 나는지까지 같이 봐드릴게요.

"""
from typing import List

def two_sum(nums: List[int], target: int) -> list: 
    hash_map = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash_map:
            j = hash_map[diff]
            return j, i
        
        hash_map[n] = i
    
    raise ValueError("No two sum solution")

# ChatGPT 정답
# def two_sum(nums: List[int], target: int) -> list:
#     seen = {}
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in seen:
#             return seen[diff], i
        
#         seen[n] = i
    
#     raise ValueError("No two sum solution")

# def move_zeroes(nums: List[int]) -> list:
#     write_idx = 0
#     for read_idx, n in enumerate(nums):
#         if n != 0:
#             nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
#             write_idx += 1

#         print(f'{nums} - nums[{read_idx}]: {nums[read_idx]}, write_idx: {write_idx}')
            
#     return nums

if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9

    # i, j = two_sum(nums, target)
    # print(i, j)

    # Problem 2 move_zeroes
    nums = [0, 0, 3, 9, 0, 10]
    nums = move_zeroes(nums)
    print(nums)