from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)

    def backtrack(idx, current):
        if idx == n:
            result.append(current[:])
            return

        current.append(nums[idx])
        backtrack(idx + 1, current)

        current.pop()
        backtrack(idx + 1, current)

    backtrack(0, [])
    return result
