def product_of_array_except_self(nums: list[int]) -> list[int]:
    if not nums:
        return []
    
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result