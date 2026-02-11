"""
좋아요. **말 없이 바로 문제** 낼게요.
이건 오늘 DFS/BFS의 **마지막 퍼즐 조각**입니다.

---

# BFS / DFS — Graph 버전

## **Connected Components in an Undirected Graph**

### 문제

정점 `n`개(`0`부터 `n-1`)로 이루어진 **무방향 그래프**가 주어집니다.
간선 목록 `edges`가 주어질 때, **연결 요소(connected components)의 개수**를 반환하세요.

---

## 입력

* `n: int` — 정점 개수
* `edges: list[list[int]]` — 무방향 간선 목록

```python
edges[i] = [u, v]  # u와 v는 연결됨
```

---

## 출력

* 연결 요소의 개수 (`int`)

---

## 예시 1

```python
n = 5
edges = [[0,1], [1,2], [3,4]]
```

그래프:

```
0 — 1 — 2    3 — 4
```

출력:

```text
2
```

---

## 예시 2

```python
n = 5
edges = [[0,1], [1,2], [2,3], [3,4]]
```

출력:

```text
1
```

---

## 예시 3 (고립 노드)

```python
n = 4
edges = []
```

출력:

```text
4
```

---

## 요구사항

* DFS **또는** BFS 사용
* 시간복잡도: **O(n + |edges|)**
* Python

함수 시그니처:

```python
def count_components(n: int, edges: list[list[int]]) -> int:
    ...
```

---

## 힌트 (최소한만)

1. adjacency list 만들기
2. visited set (또는 boolean array)
3. `0 ~ n-1` 순회하면서

   * 아직 방문 안 한 노드 발견 → component +1
   * DFS/BFS로 전부 방문 처리

> grid 문제에서 `(r,c)` 대신 **node 하나**만 다룬다고 생각하면 끝.

---

## 의도 (이 문제를 왜 내냐면)

이걸 풀면:

* DFS/BFS **개념 완전 통합**
* grid ↔ graph 차이 사라짐
* “DFS/BFS는 그냥 상태 확장 템플릿”이라는 게 몸에 박힘

---

👉 **코드 작성해서 그대로 붙여주세요.**
(DFS든 BFS든 상관없습니다. 당신 스타일로 가세요.)

"""

from collections import deque

def count_components(n: int, edges: list[list[int]]) -> int:
    visited = [0] * n
    adjacency_list = [[] for _ in range(n)]

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    def bfs(start: int):
        q = deque([start])
        visited[start] = 1

        while q:
            node = q.popleft()
            for neighbor in adjacency_list[node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    q.append(neighbor)

    count = 0
    for node in range(n):
        if visited[node] == 0:
            count += 1
            bfs(node)

    return count

            

if __name__ == "__main__":
    # n = 5
    # edges = [[0,1], [1,2], [3,4]]
    # n = 5
    # edges = [[0,1], [1,2], [2,3], [3,4]]
    n = 4
    edges = []

    print(count_components(n, edges))