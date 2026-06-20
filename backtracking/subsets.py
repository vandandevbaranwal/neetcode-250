# Pattern: Bit Manipulation (Power Set Generation)
# Trigger: "generate all subsets" = every element has two choices (include/exclude)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        # iterate through all possible bitmasks
        for i in range(1 << n):

            # include nums[j] if j-th bit is set
            subset = [
                nums[j]
                for j in range(n)
                if (i & (1 << j))
            ]

            res.append(subset)

        return res