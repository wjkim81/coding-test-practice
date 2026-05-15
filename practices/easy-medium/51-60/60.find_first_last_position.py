def search_range(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]
    
    def find_left():
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid   # 후보 저장
                r = mid - 1    # 더 왼쪽 탐색!
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return result
    
    def find_right():
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid   # 후보 저장
                l = mid + 1    # 더 오른쪽 탐색!
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return result
    
    return [find_left(), find_right()]