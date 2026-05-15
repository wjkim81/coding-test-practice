from collections import Counter

def longest_palindrome(s: str) -> int:
    if not s:
        return 0
    
    counts = Counter(s)
    longest = 0
    has_odd = False
    for count in counts.values():
        longest += count // 2 * 2
        if count % 2 == 1:
            has_odd = True

    if has_odd:
        longest += 1

    return longest
