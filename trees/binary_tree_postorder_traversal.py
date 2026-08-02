# Pattern: Recursive DFS (Postorder Traversal)
# Trigger: "postorder traversal" = visit children before the current node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            # base case
            if not node:
                return

            # traverse left subtree
            postorder(node.left)

            # traverse right subtree
            postorder(node.right)

            # visit current node
            res.append(node.val)

        postorder(root)
        return res