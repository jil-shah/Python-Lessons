# Problem 4 — Rotting Oranges
# LeetCode 994 — Medium

# Grid values:

# 0 = empty
# 1 = fresh
# 2 = rotten


# Every minute, rotten oranges infect adjacent fresh oranges.
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

# thought process 1
# so we need to find all 2 positions 
# once we have that we recursively infect the other oranges 
# first run - we expand out one level up down right left
# but we can repeat a node, so instead after we visit a node, maybe we indicate its already been visited by flipping to 0
# how do we know a minute has passed?
# thought process 2 
# the phrase every minute could indicate bfs so every level is one new minutes
# enqueue every rotten orange before BFS Starts 
# identify the number of fresh oranges - this is because the goal is for all to be infected but some could be unreachable
# go through each rotten orange and then check all directions, switch to rotten and decrease fresh 
# add other directions 

from collections import deque

def Rot(grid):
    # find the positions for -2
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if (grid[r][c] == 2):
                q.append((r,c))
            elif (grid[r][c] == 1):
                fresh += 1
    time = 0 
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    # now iterate through the q 
    while q and fresh > 0:
        for _ in range(len(q)):
            r,c = q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if (
                    0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append((nr,nc))
        time +=1
    return (time if fresh == 0 else -1)






grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(Rot(grid1))

# Expected: 4