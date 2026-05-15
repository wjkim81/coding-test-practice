from typing import List

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def word_search(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    m, n = len(board), len(board[0])
    
    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n:
            return False
        if board[r][c] != word[index]:
            return False
            
        temp = board[r][c]
        board[r][c] = '#'

        for dr, dc in DIRS:
            if dfs(r + dr, c + dc, index + 1):
                board[r][c] = temp
                return True
            
        board[r][c] = temp
        return False
                
                
                
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
                
    return False