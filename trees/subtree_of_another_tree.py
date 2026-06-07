# Pattern: Tree Serialization + Z-Function (String Matching)
# Trigger: "subtree check" = convert trees to strings = string matching problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"     # $ = delimiter, # = null node marker
        # preorder serialization: delimiter + value + left + right
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def z_function(self, s: str) -> list:
        # Z-function: z[i] = length of longest substring starting at i
        # that matches a prefix of s
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)

        # combine: pattern|text — classic Z/KMP trick
        combined = serialized_subRoot + "|" + serialized_root
        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)

        # if any position in text matches full pattern length = subtree found
        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False