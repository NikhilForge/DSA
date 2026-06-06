class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            current_price=prices[i]
            min_price=min(min_price,current_price)
            pro=current_price-min_price
            max_profit=max(max_profit,pro)
        return max_profit


        