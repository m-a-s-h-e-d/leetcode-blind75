# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    # UP, DOWN, LEFT, RIGHT
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # Do a search for connecting 1s and turn them into 0s
    # Connecting 1s means it is all part of the same island
    def dfs(row, col):
      # Bounds check
      if (row < 0 or row >= row_n) or (col < 0 or col >= col_n):
        return
      elif grid[row][col] == "0":
        return

      grid[row][col] = "0"

      # Go in every adjacent direction (horizontally and vertically)
      for direction_row, direction_col in directions:
        dfs(row + direction_row, col + direction_col)

    row_n, col_n = len(grid), len(grid[0])
    island_count = 0

    # Search for instances of 1
    for row in range(row_n):
      for col in range(col_n):
        if grid[row][col] == "1":
          # Start DFS and add to island count
          island_count += 1
          dfs(row, col)
    
    return island_count