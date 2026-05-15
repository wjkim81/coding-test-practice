def house_robber(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]

"""
prev2 = 0
prev1 = 0

for n in nums:
    prev2, prev1 = prev1, max(prev1, prev2 + n)

return prev1

"""