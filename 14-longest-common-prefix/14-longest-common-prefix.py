class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        strs.sort(key=len)
        for ch in strs[0]:
            for s in strs:
                if not s.startswith(longest + ch):
                    return longest
            longest += ch
        return longest
            