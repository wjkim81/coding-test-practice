def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    
    f_1 = 2
    f_2 = 1
    for _ in range(3, n + 1):
        f = f_1 + f_2
        f_2, f_1 = f_1, f

    return f