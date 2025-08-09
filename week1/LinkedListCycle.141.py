# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # One of the solutions can be iterate node by node over the given linked list
        # until to over the max number of nodes, 10^4. It'll be called brute force

        # But, as we need only to return true or false, what we can do is:
        # We iterate over the LL and node by node we mark the viewed nodes
        # If we find a mark, this LL has cycle, otherwise, not.

        # As -10^5 <= Node.val <= 10^5 as a constraint, we can consider that Node.val = -10^5 - 1 is a mark

        if head is None or head.next is None: # Cover the cases of empty LL and single node LL 
            return None

        while head is not None:
            if head.val == -100001:
                return True
            head.val = -100001
            head = head.next   

        return False



