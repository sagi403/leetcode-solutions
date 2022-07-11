class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = dic[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            curr = s[i]
            prev = s[i + 1]
            if dic[curr] < dic[prev]:
                res -= dic[curr]
            else:
                res += dic[curr]
        return res