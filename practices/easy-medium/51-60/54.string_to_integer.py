def string_to_integer(s: str) -> int:
    if not s:
        return 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    i = 0
    n = len(s)
    
    while i < n and s[i] == ' ':
        i += 1
    
    if i == n:
        return 0
    
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1
    
    num = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN
        num = num * 10 + digit
        i += 1
    
    return sign * num