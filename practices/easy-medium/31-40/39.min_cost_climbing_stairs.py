def min_cost_climbing_stairs(cost: list[int]) -> int:
    if not cost:
        return 0
    if len(cost) == 1:
        return cost[0]
    
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = min(cost[1], cost[0])
    
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[-1], dp[-2])