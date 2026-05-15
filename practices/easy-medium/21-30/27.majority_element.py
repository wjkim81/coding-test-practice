def majority_element(nums: list[int]) -> int:
    majority = nums[0]
    count = 1

    for n in nums[1:]:
        if n == majority:
            count += 1
        else:
            count -= 1
        
            if count == 0:
                majority = n
                count = 1

    return majority