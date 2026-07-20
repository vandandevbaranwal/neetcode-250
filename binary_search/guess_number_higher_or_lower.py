# Pattern: Classic Binary Search
# Trigger: "search a hidden number using feedback" = binary search

# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            # choose the middle number
            m = (l + r) // 2

            # ask the API
            res = guess(m)

            # picked number is larger
            if res > 0:
                l = m + 1

            # picked number is smaller
            elif res < 0:
                r = m - 1

            # correct guess
            else:
                return m
                