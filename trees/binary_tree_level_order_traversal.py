# Pattern: BFS Level Order — process nodes layer by layer using queue
# Trigger: "level order" = process by levels = BFS with snapshot of queue size per level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)    # snapshot current level size
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)   # add children for next level
                    q.append(node.right)  # None children handled by if node check

            if level:
                res.append(level)         # only append non-empty levels

        return res
    
    