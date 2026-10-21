# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        temp = head

        p1 = head
        p2 = head

        while p1!=None and p2!=None:
            while p2!=None and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p2
        
        return head