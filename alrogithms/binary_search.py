def binary_search(nums: list[int], target: int) -> int:
    """
    Args:
        nums: 오름차순 정렬된 배열
        target: 찾을 값
    
    Returns:
        target의 인덱스, 없으면 -1
    """
    def binary_search(nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

if __name__ == "__main__":
    print("start")
    # 기본
    binary_search([1, 3, 5, 7, 9], 5)  # → 2
    binary_search([1, 3, 5, 7, 9], 1)  # → 0
    binary_search([1, 3, 5, 7, 9], 9)  # → 4

    # 없는 경우
    binary_search([1, 3, 5, 7, 9], 4)  # → -1
    binary_search([1, 3, 5, 7, 9], 0)  # → -1

    # Edge cases
    binary_search([], 5)              # → -1
    binary_search([5], 5)             # → 0
    binary_search([5], 3)             # → -1