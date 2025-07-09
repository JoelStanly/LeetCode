# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        currentnode = head
        while currentnode:
            print(currentnode.val)
            if currentnode in visited:
                return True
            visited.add(currentnode)
            currentnode = currentnode.next
        return False
        