"""
네, 그 증거면 **Coursera에서 실제로 수강/완료한 게 맞습니다.**
(과목명, 강의자, 완료 날짜(2019-02-08), 학습 기간, 점수(93.33%)까지 구체적으로 적혀 있어서 “내가 예전에 했던 것 같은데?” 수준이 아니라 **완료 기록**이에요.)
그리고 2019년에 배운 DFS/BFS를 지금 까먹은 것도 **정상**입니다. 실무에서 자주 안 쓰면 1–2년만 지나도 구현 디테일은 빠집니다.

이제 바로 **Number of Islands (DFS)** 갑니다.

---

# Problem: Number of Islands (DFS)

## 문제

`grid`는 `'1'`(land)와 `'0'`(water)로 이루어진 2D 배열입니다.
상하좌우로 연결된 `'1'`들의 덩어리를 하나의 섬이라고 할 때, 섬의 개수를 반환하세요.

### 예시

입력:

```
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

출력: `3`

---

## 구현 포인트(실수 방지용)

* 전체 grid를 스캔하면서 `'1'`을 찾는다.
* `'1'`을 만나면:

  * 섬 개수 +1
  * DFS로 연결된 `'1'`을 전부 `'0'`으로 바꿔서 **재방문 방지**
* DFS의 base condition은 두 개:

  * 범위 밖이면 return
  * 물(`'0'`)이면 return

---

## 코테 시그니처

```python
def num_islands(grid: list[list[str]]) -> int:
    ...
```

---

## 당신이 바로 구현할 때 기억해야 할 한 문장

> “(r,c) 들어오면 먼저 0으로 바꾸고, 사방으로 재귀한다.”

---

## 이제 코드 작성

아래 두 케이스를 통과하도록 작성해서 붙여주세요.

### Test 1

```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# expected: 3
```

### Test 2

```
grid = [
  ["1","1","1"],
  ["0","1","0"],
  ["1","1","1"]
]
# expected: 1
```

---

작성해 주시면 제가:

* recursion depth 위험 여부
* 방문 처리 위치
* edge case (빈 grid)
* 면접에서 말하는 15초 설명

까지 깔끔하게 리뷰해 드리겠습니다.

"""
from collections import deque

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def num_islands_bfs(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    n_rows, n_cols = len(grid), len(grid[0])
    count = 0

    def bfs(r: int, c: int):
        q = deque([(r, c)])
        grid[r][c] = '0'

        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    q.append((nr, nc))

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)

    return count

def num_islands_dfs(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    n_rows, n_cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int):
        # base conditions
        if not (0 <= r < n_rows and 0 <= c < n_cols):
            return
        if grid[r][c] != '1':
            return

        # mark visited
        grid[r][c] = '0'

        # explore neighbors
        for dr, dc in dirs:
            dfs(r + dr, c + dc)

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count

if __name__ == "__main__":
    # grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]
    # expected: 3

    grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    # # expected: 1

    print(num_islands_bfs(grid))



