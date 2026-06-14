# Pattern: Iterative Tree Construction — use preorder + inorder to rebuild tree
# Trigger: "construct tree from traversals" = preorder gives root, inorder gives left/right split

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)

        while i < n and j < n:
            # preorder[i] is always the next root — add as right child with thread back
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            i += 1

            # keep going left while current node isn't the inorder boundary
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1

            # inorder[j] matched — we've found all left children of this node
            j += 1

            # climb back up using threads while inorder matches
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None    # remove thread
                curr = prev
                j += 1

        return head.right