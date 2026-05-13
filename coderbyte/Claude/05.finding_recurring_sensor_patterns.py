def most_frequent_subarray(events: list[int], k: int) -> tuple[list[int], int]:
    """
    Find the k-length contiguous subarray that appears most often in `events`.

    Args:
        events: list of integer event codes.
        k:      length of the subarray to look for (k >= 1).

    Returns:
        (subarray, count) where:
            subarray is the most frequent k-length contiguous subarray (as a list).
            count    is how many times it appears.
        If multiple subarrays tie for the highest count,
        return the one whose first occurrence is earliest.

    Edge cases:
        - If len(events) < k: return ([], 0).
        - If k <= 0: raise ValueError.
    """

    if not events:
        raise ValueError("events list cannot be empty")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if len(events) < k:
        raise ValueError("events list is shorter than k")

    # Continue with the rest of the function implementation
    subarray_counts = {}
    for i in range(len(events) - k + 1):
        subarray = tuple(events[i:i + k])
        subarray_counts[subarray] = subarray_counts.get(subarray, 0) + 1

    max_count = 0
    for subarray, count in subarray_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_subarray = subarray
        
    return list(most_frequent_subarray), max_count