from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)

    def backtrack(current, seen):
        if len(current) == n:
            result.append(current[:])
            return

        for num in nums:
            if num not in seen:
                current.append(num)
                seen.add(num)

                backtrack(current, seen)

                current.pop()
                seen.remove(num)

    backtrack([], set())
    return result
