# Pattern: Mathematical Library Function
# Trigger: "compute integer square root" = use built-in sqrt

from math import sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt() returns a floating-point value
        # int() truncates the decimal part
        return int(sqrt(x))