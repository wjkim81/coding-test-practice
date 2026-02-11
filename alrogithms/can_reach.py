from collections import deque


dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def can_reach_bfs(grid: list[list[int]]) -> bool:
    """BFS로 도달 가능 여부 반환"""
    if not grid or not grid[0]:
        return False
    
    n, m = len(grid), len(grid[0])
    if grid[0][0] == 0 or grid[n-1][m-1] == 0:
        return False
    
    if n == 1 and m == 1 and grid[0][0] == 1: # edge case
        return True
    
    queue = deque([(0, 0)])
    grid[0][0] = 0

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # print(f"({nr}, {nc})")
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                if nr == n - 1 and nc == m - 1:
                    return True
                grid[nr][nc] = 0
                queue.append((nr, nc))

    return False

def can_reach_dfs1(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False
    
    n, m = len(grid), len(grid[0])
    reached = False
    
    def dfs(r: int, c: int):
        nonlocal reached  # ← 이거 추가!
        
        if reached:  # 이미 찾았으면 더 안 해도 됨
            return
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        if grid[r][c] == 0:
            return
        
        if r == n - 1 and c == m - 1:
            reached = True
            return
        
        grid[r][c] = 0
        for dr, dc in dirs:
            dfs(r + dr, c + dc)

    dfs(0, 0)
    return reached


def can_reach_dfs(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False
    
    n, m = len(grid), len(grid[0])
    
    def dfs(r: int, c: int) -> bool:
        if r < 0 or r >= n or c < 0 or c >= m:
            return False
        if grid[r][c] == 0:
            return False
        if r == n - 1 and c == m - 1:
            return True
        
        grid[r][c] = 0  # 방문 처리
        
        for dr, dc in dirs:
            if dfs(r + dr, c + dc):
                return True
        
        return False

    return dfs(0, 0)

if __name__ == "__main__":
    # 도달 가능
    grid1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    print(can_reach_bfs(grid1))  # → True
    grid1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    print(can_reach_dfs(grid1))  # → True

    # 도달 불가
    grid2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(can_reach_bfs(grid2))  # → False
    grid2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(can_reach_dfs(grid2))  # → False

    # Edge cases
    grid3 = [[1]]         # → True (시작=끝)
    print(can_reach_bfs(grid3))  # → True
    grid3 = [[1]]         # → True (시작=끝)
    print(can_reach_bfs(grid3))  # → True

    grid4 = [[0]]         # → False (시작점이 벽)
    print(can_reach_bfs(grid4))  # → False
    grid4 = [[0]]
    print(can_reach_dfs(grid4))  # → False

    grid5 = [[1, 0], [0, 1]]  # → False
    print(can_reach_bfs(grid5))  # → False
    grid5 = [[1, 0], [0, 1]]
    print(can_reach_dfs(grid5))  # → False