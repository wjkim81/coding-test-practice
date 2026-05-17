from collections import deque

def fleet_max_speed_window(
    speeds: list[float],
    window_size: int
) -> list[float]:
    """
    For each index i (i >= window_size - 1), 
    return max of speeds[i - window_size + 1 : i + 1].
    
    For i < window_size - 1, skip (not enough data).
    """
    if len(speeds) < window_size:
        return []
    
    dq = deque()
    result = []

    for i in range(len(speeds)):
        # 1. Window 밖으로 나간 index 제거
        if dq and dq[0] < i - window_size + 1:
            dq.popleft()

        # 2. 새 값보다 작거나 같은 거 뒤에서 제거 (절대 max 못 됨)
        while dq and speeds[dq[-1]] <= speeds[i]:
            dq.pop()

        # 3. 현재 index push
        dq.append(i)

        # 4. Window 다 찼으면 max (deque 앞) 기록
        if i >= window_size - 1:
            result.append(speeds[dq[0]])

    return result