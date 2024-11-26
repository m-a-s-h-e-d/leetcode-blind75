# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    currentMax = 0
    currentBuy = -1
    currentSell = -1

    for price in prices:
      if currentBuy == -1 or price < currentBuy:
        currentBuy = price
      currentSell = price
      currentMax = max(currentMax, currentSell - currentBuy)
    
    return currentMax