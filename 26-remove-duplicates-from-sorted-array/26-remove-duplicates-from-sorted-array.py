class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        checker = nums[0]
        for i in range(1, len(nums)):
            if checker == nums[k]:
                nums.pop(k)
            else:
                checker = nums[k]
                k += 1
        return k
            