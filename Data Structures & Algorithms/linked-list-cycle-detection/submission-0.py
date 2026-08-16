# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        node_set = set()
        
        while head:
            if (head.val, head.next) not in node_set:
                node_set.add((head.val, head.next))
                head = head.next
            else:
                return True

        return False