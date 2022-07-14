class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", "]": "[", ")":"("}
        openPare = ["(", "[", "{"]
        check = []
        for ch in s:
            if ch in openPare:
                check.append(ch)
            elif check and dic[ch] == check[-1]:
                check.pop()
            else:
                return False
        return len(check) == 0
                
                