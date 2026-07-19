# Pattern: Binary Search (Lower Bound)
# Trigger: "find target or insertion position in a sorted array" = binary search for first element >= target

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # default insertion position is at the end
        res = len(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # target found
            if nums[mid] == target:
                return mid

            # possible insertion position
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res