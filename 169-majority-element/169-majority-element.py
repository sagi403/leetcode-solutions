class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None
        for num in nums:
            if count == 0:
                cand = num
            count += 1 if cand == num else -1
        return cand