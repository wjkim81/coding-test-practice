from typing import List
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS version
def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or not image[0]:
        return []
    
    rows, cols = len(image), len(image[0])

    old_color = image[sr][sc]
    if old_color == color:
        return image
    q = deque()
    q.append((sr, sc))
    image[sr][sc] = color

    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color:
                image[nr][nc] = color
                q.append((nr, nc))

    return image

# DFS Version
def flood_fill_dfs(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image or not image[0]:
        return image

    rows, cols = len(image), len(image[0])
    old_color = image[sr][sc]

    if old_color == color:
        return image

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != old_color:
            return

        image[r][c] = color

        for dr, dc in DIRS:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image
