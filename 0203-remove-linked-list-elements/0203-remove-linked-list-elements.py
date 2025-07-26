# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0)
        output = ans
        while head:
            if head.val != val:
                temp = ListNode(head.val)
                ans.next = temp
                temp = temp.next
                ans = ans.next
            head = head.next
        return output.next