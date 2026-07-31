class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = r = 0
        while r < len(prices)-1:
            r += 1
            if prices[r] < prices[r-1]:
                best = max(best, prices[r-1] - prices[l])
            while prices[r] < prices[l]:
                l += 1
        
        return max(best, prices[r] - prices[l])

