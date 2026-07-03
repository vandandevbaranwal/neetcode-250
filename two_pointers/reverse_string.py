# Pattern: Two Pointers (Opposite Ends)
# Trigger: "reverse array/string in-place" = swap elements from both ends

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # initialize pointers at both ends
        l, r = 0, len(s) - 1

        while l < r:

            # swap left and right characters
            s[l], s[r] = s[r], s[l]

            # move pointers inward
            l += 1
            r -= 1