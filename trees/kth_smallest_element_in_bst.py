# Pattern: Morris Traversal — inorder traversal with O(1) space using threaded pointers
# Trigger: "kth smallest in BST" = inorder gives sorted order = Morris for O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left:
                # no left child — visit current node
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                # find inorder predecessor (rightmost node in left subtree)
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    # create thread — link predecessor back to current
                    pred.right = curr
                    curr = curr.left
                else:
                    # thread already exists — remove it, visit current node
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1
    