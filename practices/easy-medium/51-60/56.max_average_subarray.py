def find_max_average(nums: list[int], k: int) -> float:
    if k <= 0 or k > len(nums):
        return 0.0

    k_sum = sum(nums[:k]) # initial sum from 0 to k-1
    best = k_sum / k

    for right in range(k, len(nums)):
        k_sum = k_sum - nums[right - k] + nums[right]
        best = max(best, k_sum / k)

    return best