# Pattern: Level Order Traversal (BFS)
# Trigger: "right side view" = take the last visible node at each level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            # process one level at a time
            for i in range(qLen):
                node = q.popleft()

                if node:
                    rightSide = node  # keeps updating, ends as rightmost node

                    q.append(node.left)
                    q.append(node.right)

            # add the last non-null node from this level
            if rightSide:
                res.append(rightSide.val)

        return res