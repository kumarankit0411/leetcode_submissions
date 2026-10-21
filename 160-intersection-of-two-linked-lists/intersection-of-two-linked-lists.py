# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        c1 = 0
        c2 = 0

        while p1.next is not None:
            p1 = p1.next
            c1+=1
        
        while p2.next is not None:
            p2 = p2.next
            c2+=1

        if c1 > c2:
            diff = c1 - c2
            while diff > 0:
                headA = headA.next
                diff-=1
        elif c2 > c1:
            diff = c2 - c1
            while diff > 0:
                headB = headB.next
                diff-=1
        
        while headA is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None


        
        
