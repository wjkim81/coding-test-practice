def insert_interval(intervals: list, newInterval: list) -> list:
    if not intervals:
        return [newInterval]
    
    out = []
    i = 0
    n = len(intervals)
    
    # 1. 겹치지 않는 앞부분
    while i < n and intervals[i][1] < newInterval[0]:
        out.append(intervals[i])
        i += 1
    
    # 2. 겹치는 부분 병합
    merged = newInterval[:]
    while i < n and intervals[i][0] <= merged[1]:
        merged[0] = min(merged[0], intervals[i][0])
        merged[1] = max(merged[1], intervals[i][1])
        i += 1
    out.append(merged)
    
    # 3. 겹치지 않는 뒷부분
    while i < n:
        out.append(intervals[i])
        i += 1
    
    return out