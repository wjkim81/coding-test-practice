from collections import deque

def sliding_window_max(nums: list, k: int) -> list:
    dq = deque()   # 인덱스 저장
    result = []
    
    for i in range(len(nums)):
        # 1. 앞: 윈도우 밖으로 나간 인덱스 제거
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 2. 뒤: 현재보다 작은 거 제거 (어차피 최대 못 됨)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # 3. 현재 인덱스 추가
        dq.append(i)
        
        # 4. 윈도우 완성되면 결과 추가
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result