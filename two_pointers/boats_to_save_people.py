# Pattern: Two Pointers + Greedy
# Trigger: "pair people/items under a limit" = sort and match the lightest with the heaviest

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people by weight
        people.sort()

        res = 0
        l = 0
        r = len(people) - 1

        while l <= r:

            # always place the heaviest remaining person in a boat
            remain = limit - people[r]
            r -= 1
            res += 1

            # if the lightest person fits, pair them together
            if l <= r and remain >= people[l]:
                l += 1

        return res