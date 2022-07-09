class Solution:
    def isPalindrome(self, x: int) -> bool:
        intToStr = str(x)
        for i in range(len(intToStr)):
            if intToStr[i] != intToStr[-1-i]:
                return False
        return True