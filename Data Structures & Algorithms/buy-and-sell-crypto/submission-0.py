class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        op = 0
        for p in prices[1:]:
            low = min(low,p)
            op = max(op,p-low)
        return op
        