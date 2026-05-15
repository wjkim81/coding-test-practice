def search_rotated_array(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:  # 왼쪽 정렬됨
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:  # 오른쪽 정렬됨
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1