# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1,2,3,4,5] -> [5,4,3,2,1]
        # [1,2,3] -> [3,2,1]
        # [1] -> [1]
        # [] -> []

        # Our 1st approach can be to iterate by the list
        # Then, we find the list's tail 
        # And we iterate going back changing the reference of each node
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if head is None:
            return None

        current = head
        stack = []

        while current is not None and current.next is not None:
            stack.append(current.val)
            current = current.next
        
        reversed_list = ListNode(current.val)
        tail = reversed_list

        while stack:
            tail.next = ListNode(stack.pop())
            tail = tail.next

        return reversed_list
        

        


