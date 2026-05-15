def daily_temperatures(temps: list[int]) -> list[int]:
    result = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result
