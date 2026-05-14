def move_zeros(nums: list[int]) :
    left = 0

    for right, n in enumerate(nums):
        if n != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1