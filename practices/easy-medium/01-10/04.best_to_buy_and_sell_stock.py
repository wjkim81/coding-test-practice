from typing import List

def best_time_to_buy_and_sell(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        cur_price = prices[i]
        profit = cur_price - min_price
        min_price = min(min_price, cur_price)
        max_profit = max(max_profit, profit)

    return max_profit