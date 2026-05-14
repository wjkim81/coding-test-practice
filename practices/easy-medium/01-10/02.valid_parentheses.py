
PAIRS = {
    ')': '(',
    ']': '[',
    '}': '{',
}

def is_valid(s: str) -> bool:
    if not s:
        return True
    
    stack = [] # list as stack

    for ch in s:
        if ch in PAIRS:
            if not stack:
               return False
           
            last_ch = stack.pop()
            if last_ch != PAIRS[ch]:
               return False
        else:
            stack.append(ch)
           
    return not stack