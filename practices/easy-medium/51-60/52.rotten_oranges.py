from typing import List
from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oranges_rotting(oranges: List[List[int]]) -> int:
    if not oranges or not oranges[0]:
        return 0
    rows, cols = len(oranges), len(oranges[0])
    q = deque()
    fresh_count = 0
    for r in range(rows):
        for c in range(cols):
            if oranges[r][c] == 2:
                q.append((r, c))
            elif oranges[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    minutes = 0
    while q and fresh_count > 0:
        minutes += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and oranges[nr][nc] == 1:
                    oranges[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc))

    if fresh_count >  0:
        return -1
    return minutes