class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        curr_x = x
        new_x = 0
        while curr_x > 0:
            num = curr_x % 10
            curr_x = curr_x // 10
            new_x = new_x * 10 + num
        return new_x == x