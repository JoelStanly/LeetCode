# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        while head:
            temp = ListNode(head.val)
            temp.next = output.next
            output.next = temp
            head = head.next
        return output.next