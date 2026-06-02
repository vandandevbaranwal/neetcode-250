# Pattern: BFS (Level Order) — process each node level by level using a queue
# Trigger: "invert/mirror tree" = swap left and right at every node = BFS or DFS both work

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            # swap left and right children
            node.left, node.right = node.right, node.left

            # add children to queue for processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root