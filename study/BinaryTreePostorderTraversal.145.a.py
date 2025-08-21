# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes = []
        _postorderTraversal(root)

    return nodes

    def _postorderTraversal(self, root: Optional[TreeNode], nodes: List[int]) -> None:
        if root is None
            return None

        _postorderTraversal(root.left, nodes)
        _postorderTraversal(root.right, nodes)
        nodes.append(root.val)

    