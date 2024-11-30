# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Flip
    for i in range(0, n // 2):
      for j in range(0, n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j] 
    
    # Transpose
    for i in range(0, n):
      for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
