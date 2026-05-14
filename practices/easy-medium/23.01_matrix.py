from typing import List
from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def shortest_path_from_zero(grid: List[List[int]]) -> List[List[int]]:
    if not grid or not grid[0]:
        return []
    rows, cols = len(grid), len(grid[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                q.append((r, c))
            else:
                grid[r][c] = float('inf')
    distance = 0
    while q:
        distance += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == float('inf'):
                    grid[nr][nc] = distance
                    q.append((nr, nc))
    return grid