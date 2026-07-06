# Pattern: Two Pointers (Reverse Merge)
# Trigger: "merge two sorted arrays in-place" = fill from the end to avoid overwriting

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # last position to fill in nums1
        last = m + n - 1

        # pointers to the last valid elements
        i = m - 1
        j = n - 1

        # keep merging until nums2 is exhausted
        while j >= 0:

            # place the larger element at the end
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1

            # move to the next position from the end
            last -= 1