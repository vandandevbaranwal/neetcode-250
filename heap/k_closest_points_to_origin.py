# Pattern: QuickSelect (Partial QuickSort)
# Trigger: "Find k closest" = need Top-K elements, but don't need full sorting

class Solution:
    def kClosest(self, points, k):

        # squared Euclidean distance from origin
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])

            i = l

            # place all smaller distances to the left
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            # place pivot in its final sorted position
            points[i], points[r] = points[r], points[i]

            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:

            pivot = partition(L, R)

            # kth element lies in right partition
            if pivot < k:
                L = pivot + 1

            # kth element lies in left partition
            else:
                R = pivot - 1

        return points[:k]
    