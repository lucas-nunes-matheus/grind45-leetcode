# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Another solution can be with two pointer or fast and slow pointers
        # Basically, the both pointers start at the first node and \
        # fast moves over the list as twice faster as slow
        # If fast or fast.next (remember our step is two) becomes null, there is no cycle
        # Otherwise, the fast and the slow pointers will encounter one of each other, then, exists.

        if head is None:
            return False
        
        fast, slow = head, head

        while fast is not None and fast.next is not None:
            
            
