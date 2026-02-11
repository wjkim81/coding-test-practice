"""
좋습니다. **Day 10은 LRU Cache를 “설계 설명 중심”으로 정리하고 종료**하는 전략이 가장 효율적입니다.
아래는 **코테·라이브 인터뷰에서 그대로 말로 설명할 수 있는 수준**을 목표로 구성했습니다.

---

# Day 10 — LRU Cache (설계 중심)

## 1️⃣ 문제 정의 (정확히)

**LRU Cache (Least Recently Used Cache)** 는 다음을 지원하는 자료구조입니다.

* `get(key)`

  * key가 있으면 value 반환
  * 없으면 `-1`
  * **접근된 항목은 “가장 최근에 사용됨”으로 갱신**

* `put(key, value)`

  * key가 있으면 value 갱신 + 최근 사용으로 갱신
  * key가 없고 capacity 초과 시
    → **가장 오래 사용되지 않은 항목 제거**

### 성능 요구사항

> **모든 연산을 평균 O(1)** 에 수행해야 함

---

## 2️⃣ 왜 단순한 자료구조로는 안 되는가?

### dict만 쓰면?

* key → value 접근 O(1) ✔
* 하지만 **“가장 오래 안 쓴 것”을 O(1)로 찾을 수 없음 ❌**

### list만 쓰면?

* 순서 관리 가능 ✔
* 하지만 삭제/이동이 O(n) ❌

👉 **두 가지를 동시에 만족해야 함**

---

## 3️⃣ 핵심 아이디어 (이게 전부)

> **HashMap + Doubly Linked List**

* **HashMap (dict)**

  * key → node
  * O(1) 접근

* **Doubly Linked List**

  * 사용 순서 유지
  * head = 가장 최근 사용
  * tail = 가장 오래 사용
  * O(1) 삽입/삭제

이 조합이 **유일하게 조건을 만족**합니다.

---

## 4️⃣ 구조를 그림 없이 말로 설명하면

* 각 cache entry는 **linked list의 node**

* node에는:

  * `key`
  * `value`
  * `prev`, `next`

* dict는:

  ```text
  key → 해당 node
  ```

* linked list는:

  ```text
  head <-> ... <-> tail
  ```

* 항상 유지되는 규칙:

  * **최근에 접근한 node는 head 쪽**
  * **제거 대상은 tail 바로 앞**

---

## 5️⃣ 더미 노드를 쓰는 이유 (중요)

```text
dummy_head <-> ... <-> dummy_tail
```

이렇게 두 개의 dummy node를 둡니다.

### 이유

* head/tail edge case 제거
* 삽입/삭제 로직 단순화
* if 문 최소화

👉 연결 리스트를 안정적으로 다루는 **정석 패턴**

---

## 6️⃣ 연산별 동작 설명 (말로 설명하는 버전)

### 🔹 get(key)

1. dict에 key 없으면 `-1`
2. 있으면 node 찾기 (O(1))
3. 해당 node를 **head 쪽으로 이동**
4. value 반환

### 🔹 put(key, value)

* key가 이미 있음:

  1. value 업데이트
  2. node를 head로 이동

* key가 없음:

  1. 새 node 생성
  2. head에 삽입
  3. dict에 등록
  4. capacity 초과 시:

     * tail 쪽 node 제거
     * dict에서도 제거

---

## 7️⃣ 시간·공간 복잡도

* `get`: O(1)
* `put`: O(1)
* 공간: O(capacity)

👉 **이 문제의 핵심은 “구현”이 아니라 “이 복잡도가 왜 성립하는지” 설명하는 것**

---

## 8️⃣ 면접에서 가장 좋은 20초 설명 (암기용)

> “LRU Cache requires O(1) get and put. I use a hashmap for fast lookup and a doubly linked list to maintain usage order. On access, I move the node to the head. When capacity is exceeded, I evict the node at the tail.”

이 문장 하나면 **시니어 톤으로 충분**합니다.

---

## 9️⃣ 라이브 코딩이 나온다면? (현실 조언)

* **30분 코테에 구현까지 요구되면 난이도 높은 편**
* 하지만 보통은:

  * 설계 설명
  * 핵심 로직 일부
  * 또는 skeleton 제공

지금 수준이면:

* **설계 질문 → 완벽 대응 가능**
* 구현은 복습하면서 한 번 정도만 손에 익히면 충분

---

## 🔟 오늘 Day 10의 “완료 기준”

아래가 말로 자연스럽게 나오면 **완료**입니다.

* 왜 dict + doubly linked list인가
* head / tail의 의미
* eviction이 왜 O(1)인가
* dummy node를 왜 쓰는가

---

## 다음 진행 방식 (합의된 플랜)

* ✅ **Day 10: LRU Cache 설명 중심으로 종료**
* 🔁 이후:

  * 코테 문제는 **본인이 복습하면서 1~2문제씩**
  * 필요할 때 질문만 가져오기

이 방식이 **가장 피로도 낮고, 합격 확률이 높은 루트**입니다.

필요하면 다음에:

* **LRU Cache 구현 최소 버전**
* **“이 자료구조를 ML 시스템에서 어떻게 쓰는지” 연결 설명**
* **시험 직전 10분 요약본**

중 하나를 바로 도와드릴게요.

"""

class Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy head/tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- internal helpers ---
    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        # Insert right after head
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        # LRU is right before tail
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]

    # --- public API ---
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node is not None:
            node.val = value
            self._move_to_front(node)
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.cap:
            self._evict_lru()
