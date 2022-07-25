class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        n = 1
        sqrt = 1
        while sqrt < x:
            sqrt = n * n
            n += 1
        if sqrt == x:
            return n - 1
        elif sqrt > x:
            return n - 2