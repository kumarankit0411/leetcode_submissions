# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head

        while slow!=None:
            if fast == None or fast.next==None:
                return False
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            if slow == fast:
                return True
        
        return False