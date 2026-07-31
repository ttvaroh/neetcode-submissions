class Solution:
    def fillIsland(self, grid: List[List[str]], row: int, col: int, val: str) -> None:
            inRange = 0 <= row < len(grid) and 0 <= col < len(grid[row])
            if not inRange or grid[row][col] != "1":
                return
            grid[row][col] = val
            self.fillIsland(grid, row+1, col, val)
            self.fillIsland(grid, row-1, col, val)
            self.fillIsland(grid, row, col+1, val)
            self.fillIsland(grid, row, col-1, val)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 1
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != "1": continue
                count += 1
                self.fillIsland(grid, row, col, str(count))
        return count - 1
