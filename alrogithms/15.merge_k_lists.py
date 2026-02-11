"""
## Day 8-2️⃣

## **Merge K Sorted Lists** (Medium)

이 문제는 **Heap 문제의 정수 버전이 아니라 ‘포인터 + 힙’ 문제**입니다.

---

### 문제

정렬된 연결 리스트 `k`개가 주어질 때,
모든 리스트를 하나의 정렬된 리스트로 병합하라.

---

### 핵심 사고 (이것만 기억)

* 각 리스트의 **현재 포인터(head)** 만 heap에 넣는다
* heap에는 항상 **“다음 후보”만** 존재
* pop → 결과에 연결 → 그 노드의 next를 heap에 push

---

### heap에 무엇을 넣을까?

Python에서는 노드 비교가 안 되므로:

```python
(value, list_index, node)
```

형태로 넣습니다.

---

### 시그니처

```python
def merge_k_lists(lists: list[ListNode]) -> ListNode:
    ...
```

---

### 정답 코드 (가장 안전한 버전)

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

---

### 면접에서 말하는 15초 설명

> “I push the head of each list into a min-heap. Each pop gives the smallest current node, and I then push its next node. This keeps the heap size at most k.”

---

## 🔥 오늘 안에 “마무리” 기준 체크리스트

오늘 끝나면, 아래가 **머릿속에 자동으로 떠오르면 성공**입니다.

* Heap = Top-K / Merge streams
* Min-heap으로 Kth largest 푸는 이유 설명 가능
* `heapq` API 안 보고 사용 가능
* BFS / DFS / Binary search / Prefix sum / Interval / Heap
  → **전부 한 번씩 손으로 써봄**

---

## 마지막 현실 조언 (중요)

지금 느끼는 이 상태:

> “ML 기본 코딩도 해야 되는데, 준비할 게 많다…”

이건 **당연한 압박**이고,
그래서 더더욱 **코테는 여기서 닫아야** 합니다.

오늘:

* Day 8 두 문제 ✔
* 전체 패턴 10분 요약 ✔

이면 **충분히 준비된 상태**입니다.

---

다음 액션 선택해 주세요:
1️⃣ **Kth Largest부터 직접 다시 써보기**
2️⃣ **Merge K Sorted Lists 바로 복습 모드**
3️⃣ **코테 전날용 ‘패턴 한 장 요약’ 만들어 달라**

가장 필요한 걸로 바로 갑시다.
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy

    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next

    return dummy.next

def print_list(head):
    curr = head
    out = []
    while curr:
        out.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(out))


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
            print(f"init: {heap}")

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            print(f"push: {heap}")

    return dummy.next


if __name__ == "__main__":
    l1 = [1, 4, 5]
    l2 = [1, 3, 4]
    l3 = [2, 6]

    node_list = [l1, l2, l3]
    lists = []
    for l in node_list:
        linked_list = build_linked_list(l)
        lists.append(linked_list)


    merged = merge_k_lists(lists)

    print_list(merged)