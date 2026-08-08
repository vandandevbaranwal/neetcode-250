# Pattern: Backtracking / Subset Generation
# Trigger: "calculate something for every subset" = generate all subsets

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, subset):
            nonlocal res

            # calculate XOR of the current subset
            xorr = 0
            for num in subset:
                xorr ^= num

            # add this subset's XOR to the answer
            res += xorr

            # choose each remaining number
            for j in range(i, len(nums)):
                subset.append(nums[j])

                # explore subsets containing nums[j]
                backtrack(j + 1, subset)

                # undo the choice
                subset.pop()

        # start with the empty subset
        backtrack(0, [])

        return res