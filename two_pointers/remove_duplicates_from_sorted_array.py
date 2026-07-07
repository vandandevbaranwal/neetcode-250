# Pattern: Two Pointers (Slow & Fast)
# Trigger: "remove duplicates from a sorted array in-place" = fast pointer scans, slow pointer writes uniques

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)

        # l = next position to write a unique element
        # r = scans the array
        l = r = 0

        while r < n:

            # write the current unique value
            nums[l] = nums[r]

            # skip all duplicates of nums[l]
            while r < n and nums[r] == nums[l]:
                r += 1

            # move write pointer to the next position
            l += 1

        return l