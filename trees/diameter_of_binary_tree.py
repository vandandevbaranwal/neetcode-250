# Pattern: Iterative DFS (Postorder) — process children before parent using hashmap
# Trigger: "diameter" = longest path through any node = left height + right height at each node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}  # node: (height, diameter)

        while stack:
            node = stack[-1]

            # push left child if not yet processed
            if node.left and node.left not in mp:
                stack.append(node.left)
            # push right child if not yet processed
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                # both children processed — now process current node
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                # height = 1 + taller child
                # diameter = max of: path through this node, or best diameter in subtrees
                mp[node] = (
                    1 + max(leftHeight, rightHeight),
                    max(leftHeight + rightHeight, leftDiameter, rightDiameter)
                )

        return mp[root][1]  # return diameter of root