# Pattern: 2D Prefix Sum (Row-wise Prefix)
# Trigger: "multiple range sum queries" = preprocess prefix sums

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):

        # prefixSum[row][col] = sum of row elements from 0 to col
        self.prefixSum = [
            [0] * len(matrix[0])
            for _ in range(len(matrix))
        ]

        # build row-wise prefix sums
        for row in range(len(matrix)):
            self.prefixSum[row][0] = matrix[row][0]

            for col in range(1, len(matrix[0])):
                self.prefixSum[row][col] = (
                    self.prefixSum[row][col - 1]
                    + matrix[row][col]
                )

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        res = 0

        # sum each row independently
        for row in range(row1, row2 + 1):

            if col1 > 0:
                res += (
                    self.prefixSum[row][col2]
                    - self.prefixSum[row][col1 - 1]
                )
            else:
                res += self.prefixSum[row][col2]

        return res