# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
            
        if not head:
            return head
        
        currN = head
        nextN = head.next
        while nextN:
            if nextN.val == val:
                currN.next = nextN.next
            else:
                currN = nextN
            nextN = nextN.next
        return head