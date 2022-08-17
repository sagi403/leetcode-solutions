class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for ch in s:
            if (ord("A") <= ord(ch) <= ord("Z") or
                ord("a") <= ord(ch) <= ord("z") or
                ord("0") <= ord(ch) <= ord("9")):
                new_s.append(ch.lower())
        for i in range(len(new_s) - 1):
            if new_s[i] != new_s[-i-1]:
                return False
        return True