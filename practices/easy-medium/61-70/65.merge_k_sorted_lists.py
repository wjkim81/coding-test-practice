from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[ListNode | None]) -> ListNode | None:
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        _, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next