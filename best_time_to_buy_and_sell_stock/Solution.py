class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = 999999999

        for price in prices:
            if price<buy_price:
                buy_price=price
                continue
            
            if price>buy_price:
                max_profit = max(max_profit, price-buy_price)
        
        return max_profit