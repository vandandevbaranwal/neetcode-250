# Pattern: Two Pointers (Read & Write)
# Trigger: "remove elements in-place" = overwrite unwanted elements using a write pointer

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # write pointer

        # read every element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # keep current element
                k += 1             # move write pointer

        return k