# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Constraints:

1) The number of nodes in the list is in the range [1, 100].
2) 1 <= Node.val <= 100

Input: Given the head of a singly linked list, return the middle node of the linked list.
Output: If there are two middle nodes, return the second middle node.
'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next            
            slow = slow.next

        return slow