from collections import Counter, defaultdict

def find_minimum_substr(s: str, t: str) -> str:
    if not s or not t:
        return ""
    
    if len(s) < len(t):
        return ""
    
    need = Counter(t)
    have = defaultdict(int)
    required = len(need)
    formed = 0

    l = 0
    ans = (float('inf'), None, None)

    for r, ch in enumerate(s):
        have[ch] += 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            left_char = s[l]
            have[left_char] -= 1

            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1

            l += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]