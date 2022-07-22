class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        string = s.strip()
        for i in range(len(string) -1, -1, -1):
            if string[i] != " ":
                count += 1
            else:
                return count
        return count