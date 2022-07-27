class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 0, 1
        for _ in range(n):
            tmp = step1 + step2
            step1 = step2
            step2 = tmp
        return tmp
        