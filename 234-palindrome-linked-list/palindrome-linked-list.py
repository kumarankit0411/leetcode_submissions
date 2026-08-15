# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # reverse second list
        prev = None
        curr = head2

        while curr != None:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future

        while prev is not None and head is not None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True