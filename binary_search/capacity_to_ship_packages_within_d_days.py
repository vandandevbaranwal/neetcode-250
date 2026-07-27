# Pattern: Binary Search on Answer
# Trigger: "find the minimum feasible value" = binary search on the answer space

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # minimum possible capacity = heaviest package
        l = max(weights)

        # maximum possible capacity = ship everything in one day
        r = sum(weights)

        res = r

        # check if a given ship capacity is sufficient
        def canShip(cap):
            ships = 1
            currCap = cap

            for w in weights:

                # current package doesn't fit in today's ship
                if currCap < w:
                    ships += 1

                    # exceeded allowed days
                    if ships > days:
                        return False

                    currCap = cap

                # load package
                currCap -= w

            return True

        # binary search on ship capacity
        while l <= r:
            cap = (l + r) // 2

            if canShip(cap):
                res = cap
                r = cap - 1
            else:
                l = cap + 1

        return res