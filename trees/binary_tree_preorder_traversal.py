# Pattern: Recursive DFS (Preorder Traversal)
# Trigger: "preorder traversal" = visit node before its children

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            # base case
            if not node:
                return

            # visit current node
            res.append(node.val)

            # traverse left subtree
            preorder(node.left)

            # traverse right subtree
            preorder(node.right)

        preorder(root)
        return res