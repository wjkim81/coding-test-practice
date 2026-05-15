from typing import List
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def number_of_islands(grid: List[List[str]]) -> int:

    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    def bfs(r: int, c: int):
        q = deque()
        grid[r][c] = "0"
        q.append((r, c))

        while q:
            cr, cc = q.popleft()
            for dr, dc in DIRS:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
        
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                bfs(r, c)

    return count
                
