# Pattern: Sliding Window (Variable Size)
# Trigger: "minimum/maximum contiguous subarray satisfying a condition" = expand and shrink window

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left pointer and current window sum
        l = 0
        total = 0

        # stores minimum valid window length
        res = float("inf")

        # expand the window
        for r in range(len(nums)):
            total += nums[r]

            # shrink while current window satisfies the condition
            while total >= target:

                # update minimum length
                res = min(res, r - l + 1)

                # remove leftmost element
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res