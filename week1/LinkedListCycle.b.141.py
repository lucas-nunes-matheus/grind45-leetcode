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

        # if head is None or head.next is None: # Cover the cases of empty LL or single node LL
        #     return False                      # It is not more necessary, 'cause the evaluation \
                                                # happens at 'if' below

        fast, slow = head, head # Assign the two pointers

        # Check whether the list is ending or not  
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow: # If fast encouters slow, a cycle exists
                return True

        return False # Otherwise, not.

        # [1, 2, 3, 4], pos=0
        # f,s               i=0
        #     s, f          i=1
        #  f     s          i=2
        #        f  s       i=3    
        # f,s  -> Cycle exists. (i=4)          
            
            
