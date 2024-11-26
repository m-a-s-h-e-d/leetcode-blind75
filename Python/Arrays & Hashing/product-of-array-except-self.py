# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)

    # First, process the product of every previous number from left to right
    prefix = [1] * n

    for i in range(1, n):
      prefix[i] = prefix[i - 1] * nums[i - 1]
        
    # We also need to get the products from the right side
    suffix = [1] * n

    for i in range(n - 2, -1, -1):
      suffix[i] = suffix[i + 1] * nums[i + 1]

    # Now calculate all the products using the prefix and suffix (since they do not include current index)
    products = []
    
    for i in range(0, n):
      products.append(prefix[i] * suffix[i])

    return products
