from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    seen = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return seen[diff], i
        seen[n] = i

    raise ValueError("No solution found")
