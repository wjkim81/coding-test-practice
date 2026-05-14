def binary_search(nums: list[int], target: int) -> int:

    if not nums:
        return -1
    
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1