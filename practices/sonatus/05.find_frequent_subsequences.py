from collections import Counter

def find_frequent_subsequences(
    event_log: list[str],
    k: int,
    n: int
) -> list[tuple[tuple[str, ...], int]]:
    if  len(event_log) < k:
        return []
    
    windows = (tuple(event_log[i:i+k]) for i in range(len(event_log) - k + 1))
    counts = Counter(windows)
    top_n = counts.most_common(n)

    return top_n