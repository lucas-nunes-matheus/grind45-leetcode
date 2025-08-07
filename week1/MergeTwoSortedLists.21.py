# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We have to merge two sorted singly linked lists
        # As we know the lists are sorted, we can compare val by val from the both lists to keep the order
        # Then, first: we compare the values of two nodes and we pick the smaller
        # Next, we create a dummy node in order to build our new LL of the merge
        # Finally, we add node by node at this LL and we remove the first dummy node at the end

        # We check if one of the linked lists are empty, if yes, we handle it
        if list1.val is None and list2.val is None:
            return None
        if list1.val is None:
            return list2
        if list2.val is None:
            return list1

        # we start a dummy node and a pointer, "current_node" 
        dummy_node = ListNode()
        current_node = dummy_node

        p1 = list1
        p2 = list2

        while p1.val is not None and p2.val is not None:
            if p1.val < p2.val:
                current_node.next = ListNode(p1.val)
                current_node = current_node.next
                p1 = p1.next
            else:
                current_node.next = ListNode(p2.val)
                current_node = current_node.next
                p2 = p2.next

        if p1.val is not None:
            current_node.next = p1.head  
        if p2.val is not None:
            current_node.next = p2.head

        dummy_node = dummy_node.next

        return dummy_node
        



            

        