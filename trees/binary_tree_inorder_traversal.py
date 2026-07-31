# Pattern: Iterative DFS (Inorder Traversal)
# Trigger: "inorder traversal without recursion" = use a stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:

            # travel to the leftmost node
            while cur:
                stack.append(cur)
                cur = cur.left

            # process current node
            cur = stack.pop()
            res.append(cur.val)

            # move to the right subtree
            cur = cur.right

        return res