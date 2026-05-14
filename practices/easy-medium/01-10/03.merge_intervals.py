from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for cur_start, cur_end in intervals[1:]:
        last_start, last_end = merged[-1]

        if last_end >= cur_start:
            merged[-1][1] = max(last_end, cur_end)
        else:
            merged.append([cur_start, cur_end])

    return merged
