# Pattern: Binary Search (Rotated Array + Duplicates)
# Trigger: "search in rotated sorted array with duplicates" = binary search with ambiguity handling

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # target found
            if nums[m] == target:
                return True

            # left half is sorted
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right half is sorted
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # duplicates make it impossible to determine
            # which half is sorted
            else:
                l += 1

        return False