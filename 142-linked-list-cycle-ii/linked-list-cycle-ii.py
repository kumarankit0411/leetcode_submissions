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

        while slow is not None:
            if fast == None or fast.next==None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = self.hasCycle(head)

        if node:
            temp = head
            while True:
                if node == temp:
                    return node
                temp = temp.next
                node = node.next
                
        else:
            return None