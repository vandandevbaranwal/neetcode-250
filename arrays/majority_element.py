# Pattern: Hash Map / Frequency Counting
# Trigger: "find the element occurring more than n/2 times" = count frequencies

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        res = 0
        maxCount = 0

        # count frequency of each element
        for num in nums:
            count[num] += 1

            # update majority candidate
            if count[num] > maxCount:
                res = num
                maxCount = count[num]

        return res