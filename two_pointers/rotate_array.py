# Pattern: Array Reversal + Two Pointers
# Trigger: "rotate array in-place" = reverse entire array, then reverse two parts

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # handle k greater than array length
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Step 1: reverse the whole array
        reverse(0, n - 1)

        # Step 2: reverse the first k elements
        reverse(0, k - 1)

        # Step 3: reverse the remaining elements
        reverse(k, n - 1)