class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = prices[0], 0

        for i in prices:
            high = max(high, i - low)
            low = min(low, i)
        
        return high
