
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0)
    dummy.next = head

    kth = dummy
    curr = dummy
    for i in range(n):
        curr = curr.next

    while curr.next:
        kth = kth.next
        curr = curr.next

    kth.next = kth.next.next
    return dummy.next