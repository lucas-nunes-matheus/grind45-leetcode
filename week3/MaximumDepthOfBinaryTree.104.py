# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
I: Given the root of a binary tree
O: return its maximum depth.

Depth -> Num of nodes along the longest path from the root node to the farthest leaves (inclusive)

Constraints:
a) The number of nodes in the tree is in the range [0, 104].
b) -100 <= Node.val <= 100

i) can be empty.
ii) inclusive (root and leaf nodes).
iii) return an int.

examples:
i: root = [3,9,20,null,null,15,7]
o: 3

i: [1,null,2]
o: 2
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0
        self._traversal(root, max_depth)

        return max_depth

    def _traversal(self, root: Optional[TreeNode], max_value: list[int]) -> None:
        