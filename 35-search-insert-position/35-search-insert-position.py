class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        while l < r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if target < nums[mid + 1] or target == nums[mid + 1]:
                    return mid + 1
                l = mid
            else:
                if target > nums[mid + 1]:
                    return mid
                r = mid