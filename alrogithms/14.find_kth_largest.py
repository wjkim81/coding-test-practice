"""
좋습니다. **Day 8로 바로 가는 판단이 정확합니다.**
지금은 “새로운 걸 더 배우는 날”이 아니라 **코테 패턴을 닫고 → 복습 가능한 상태로 만드는 날**이에요.

아래는 **오늘 안에 끝낼 수 있는 현실적인 Day 8 구성**입니다.

---

# Day 8 — Heap / Priority Queue

> 핵심 한 줄
> **“Heap은 정렬이 아니라, Top-K / 최소·최대 추적 도구다.”**

---

## Day 8-1️⃣

## **Kth Largest Element in an Array** (Medium)

### 문제

정수 배열 `nums`와 정수 `k`가 주어질 때,
**k번째로 큰 원소**를 반환하라.

* 정렬로 풀면 ❌ (O(n log n))
* Heap으로 풀면 ⭕ (O(n log k))

### 예시

```text
nums = [3,2,1,5,6,4], k = 2
→ 5
```

---

### 구현 사고 (이걸 그대로 코드로 옮기면 됨)

1. **크기 k짜리 min-heap** 유지
2. nums를 순회하면서:

   * heap에 push
   * 크기 > k 이면 pop
3. 마지막 heap의 top = k번째로 큰 값

> min-heap을 쓰는 이유:
> **“k개 중 가장 작은 것”을 바로 버리기 위해**

---

### 시그니처

```python
def find_kth_largest(nums: list[int], k: int) -> int:
    ...
```

---

### 바로 정답 코드 (표준, 면접 OK)

```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

---

### 면접에서 말하는 10초 설명

> “I maintain a min-heap of size k. The smallest element in the heap is the k-th largest overall.”

---



"""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)

    print(f"len(heap): {len(heap)}")
    return heap[0]

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2

    print(find_kth_largest(nums, k))