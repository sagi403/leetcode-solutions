class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in dic:
                return [dic[num], i]
            dic[n] = i