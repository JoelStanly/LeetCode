# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        nextElement = None if current is None else current.next
        if nextElement == None:
            return current
        while nextElement is not None:
            if current.val == nextElement.val:
                nextElement = nextElement.next
            else:
                current.next = nextElement    
                current = nextElement
                nextElement = current.next
        current.next = None
        return head