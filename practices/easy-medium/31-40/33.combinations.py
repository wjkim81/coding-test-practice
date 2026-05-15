from typing import List

def combination(nums: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(idx, current, target):
        if target == 0:
            result.append(current[:])
            return
        
        if target < 0:
            return
        
        for i in range(idx, len(nums)):
            current.append(nums[i])
            backtrack(i, current, target - nums[i])
            current.pop()

    backtrack(0, [], target)

    return result
    

