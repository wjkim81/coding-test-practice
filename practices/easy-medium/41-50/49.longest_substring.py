def longest_substring(s: str) -> int:
    left = 0
    last_seen = {}
    best = 0
    
    for right, ch in enumerate(s):
        if ch in last_seen:
            left = max(left, last_seen[ch] + 1)
        last_seen[ch] = right
        best = max(best, right - left + 1)
    
    return best