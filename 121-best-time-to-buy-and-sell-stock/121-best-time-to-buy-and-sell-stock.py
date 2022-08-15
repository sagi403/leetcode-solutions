class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best_time = 0
        for r in range(1, len(prices)):
            best_time = max(best_time, prices[r] - prices[l])
            if prices[r] <prices[l]:
                l = r
        return best_time
            