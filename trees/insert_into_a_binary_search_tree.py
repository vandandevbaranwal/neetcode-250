# Pattern: Binary Search Tree (BST) Traversal
# Trigger: "insert a value into a BST" = follow BST property until an empty position

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # empty tree -> new node becomes the root
        if not root:
            return TreeNode(val)

        cur = root

        while True:

            # insert into the right subtree
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right

            # insert into the left subtree
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left