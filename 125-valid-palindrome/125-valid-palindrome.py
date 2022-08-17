class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for ch in s:
            if (ord("A") <= ord(ch) <= ord("Z") or
                ord("a") <= ord(ch) <= ord("z") or
                ord("0") <= ord(ch) <= ord("9")):
                new_s.append(ch.lower())
        l, r = 0, len(new_s) - 1
        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True