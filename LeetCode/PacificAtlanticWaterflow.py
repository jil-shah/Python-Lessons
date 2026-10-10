# Pacific Atlantic Water Flow

# Problem
# i want to know if there is water flowing through both oceans at a cell 
# the better question is can one ocean get to the other 
# each cell can only go top bottom, left right

# brute force
# Run dfs can i reach pacific 
# run dfs can i reach atlantic
# if both add answer 
#for every cell, dfs, explore 
# this would mean its O(n^2) where n is r*c
# instead we reverse the question can the ocean reach the cell 

# smaller problem would be can this index reach pacific/atlantic
# lots of cells will ask the same question 
# which cells can pacific reach
# this mean its the reverse question is the current cell higher than the next

# the goal is to see which cells atlantic can reach
# which cells pacific can reach and the common ones are the answer

# dfs - current cell, and then neighboring cells as long as its not already visited

# stop if already visited or outside the grid 
#dfs from top and left, and then bottom and right


def waterflow(heights):

    rows = len(heights)
    cols = len(heights[0])

    atlantic = set()
    pacific = set()
    
    directions= {
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    }
    def dfs(r,c,visited):
        visited.add((r,c))
        for dr, dc in directions:
            nr = dr+r
            nc = dc+c
            if (0 <= nr < rows
                and 0 <= nc < cols
                and (nr,nc) not in visited
                and heights[r][c] <= heights[nr][nc]
            ):
                dfs(nr,nc,visited)
    #pacific
    for c in range(cols):
        dfs(0,c,pacific)
    for r in range(rows):
        dfs(r,0,pacific)
    #atlantic
    for c in range(cols):
        dfs(rows-1,c,atlantic)
    for r in range(rows):
        dfs(r,cols-1,atlantic)

    result =[]
    for r in range(rows):
        for c in range (cols):
            if ((r,c) in pacific and (r,c) in atlantic):
                result.append([r,c])
    
    return result

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(waterflow(heights))