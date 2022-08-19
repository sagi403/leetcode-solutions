class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        check = set()
        for n in nums:
            if n in check:
                check.discard(n)
            else:
                check.add(n)
        return check.pop()