# Pattern: Recursive BST Traversal
# Trigger: "delete a node from BST" = search for the node, then handle deletion cases

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # key not found
        if not root:
            return root

        # search in the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # search in the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # node found
        else:

            # Case 1: no left child
            if not root.left:
                return root.right

            # Case 2: no right child
            elif not root.right:
                return root.left

            # Case 3: two children
            # find inorder successor (smallest node in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left

            # replace current node's value
            root.val = cur.val

            # delete the duplicate successor node
            root.right = self.deleteNode(root.right, root.val)

        return root