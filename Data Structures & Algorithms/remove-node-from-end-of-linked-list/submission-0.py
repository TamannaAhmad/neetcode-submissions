# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur, prev = head, None
        count = 0

        while cur:
            count += 1
            prev = cur
            cur = cur.next

        pos, count = count - n, 0
        cur, prev = head, None
        if not cur.next:
            return None

        while cur:
            if count == pos and prev:
                prev.next = cur.next
                return head
            elif count == pos and not prev:
                return cur.next
            count += 1
            prev = cur
            cur = cur.next

        return head