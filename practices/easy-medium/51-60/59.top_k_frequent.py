from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    num_hist = Counter(nums)
    heap = []
    
    for num, count in num_hist.items():
        heapq.heappush(heap, (count, num))
        
        if len(heap) > k:
            heapq.heappop(heap)
            
            
    return [num for count, num in heap]