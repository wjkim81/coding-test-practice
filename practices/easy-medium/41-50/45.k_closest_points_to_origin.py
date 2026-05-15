from typing import List
import heapq

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for p1, p2 in points:
        distance = p1**2 + p2**2
        heapq.heappush(heap, (-distance, [p1, p2]))
        if len(heap) > k:
            heapq.heappop(heap)

    return [point for dist, point in heap]