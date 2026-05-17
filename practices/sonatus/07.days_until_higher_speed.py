def days_until_higher_speed(daily_max_speeds: list[float]) -> list[int]:
    """
    For each index i, return the number of days until a higher speed appears.
    If no higher speed in future, return -1.
    """
    result = [-1] * len(daily_max_speeds)
    stack = []

    for i, max_speed in enumerate(daily_max_speeds):
        while stack and max_speed > daily_max_speeds[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result