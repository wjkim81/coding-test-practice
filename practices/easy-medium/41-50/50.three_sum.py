from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    out = []
    for i, n in enumerate(nums):
        if n > 0:
            break
        if i > 0 and n == nums[i-1]:
            continue
        left, right = i + 1, len(nums) -1
        while left < right:
            total = n + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                out.append([n, nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return out
            