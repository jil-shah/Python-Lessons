# Problem 2 — Number of Islands
# LeetCode 200 — Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# the plan is start at (0,0)
# if its land, then we find all neighboring land, we dont want to repeat the traversal
# any new node that is land, that is an univisited island

def numIslands(grid):
    if (grid == None):
        return 0
    rowsL = len(grid)
    colsL = len(grid[0])
    islands = 0

    def dfs(r,c):
        if (
            (r < 0 or r >= rowsL)
            or (c < 0 or c >= colsL)
            or (grid[r][c] != "1" )
        ):
            return

        grid[r][c] = "0"

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for r in range (rowsL):
        for c in range (colsL):
            if (grid[r][c] == "1"):
                islands+=1
                dfs(r,c)
    return islands


grid1 = [
        ["1", "1", "1"],
        ["1", "1", "0"],
        ["1", "0", "0"]
    ]

print(numIslands(grid1))
# Expected: 1

# Three islands
grid2 = [
        ["1", "1", "0", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"]
    ]

print(numIslands(grid2))
# Expected: 3
