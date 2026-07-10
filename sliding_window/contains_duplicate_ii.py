# Pattern: Hash Map (Value → Last Seen Index)
# Trigger: "duplicate within k distance" = store the latest index of each value

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # value -> most recent index
        mp = {}

        for i in range(len(nums)):

            # duplicate found within distance k
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True

            # update latest occurrence
            mp[nums[i]] = i

        return False