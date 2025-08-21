# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        stack = [root]
        nodes = [root.val]

        while stack:
            cur = stack[-1]

            while cur.left is not None and cur.left.val not in nodes:
                stack.append(cur.left)
                cur = cur.left
                nodes.append(cur.val)

            while cur.right is not None and cur.right.val not in nodes: 
                stack.append(cur.val)
                cur = cur.right
                nodes.append(cur.val)

            stack.pop()

        return nodes