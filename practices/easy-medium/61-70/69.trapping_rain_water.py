def trap(height: list[int]) -> int:
    if not height:
        return 0
    
    right_max_height = [0] * len(height)
    left_max_height = [0] * len(height)

    left_max = 0
    for i, h in enumerate(height):
        if h > left_max:
            left_max = h
        left_max_height[i] = left_max

    right_max = 0
    for i in range(len(height)-1, -1, -1):
        h = height[i]
        if h > right_max:
            right_max = h

        right_max_height[i] = right_max
    
    total = 0
    for i, h in enumerate(height):
        total += min(left_max_height[i], right_max_height[i])  - h
    
    return total