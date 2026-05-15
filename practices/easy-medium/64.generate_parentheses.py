from typing import List

def generate_parentheses(n: int) -> List[str]:
    result = []
    def backtrack(current: str, open_used: int, closed_used: int):
        if open_used == n and closed_used == n:
            result.append(current)
            return
        
        if open_used < n:
            backtrack(current + '(', open_used + 1, closed_used)
        if closed_used < open_used:
            backtrack(current + ')', open_used, closed_used + 1)
            
    backtrack("", 0, 0)
    return result