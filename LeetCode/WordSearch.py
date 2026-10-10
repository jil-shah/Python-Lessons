# 6. Problem 5 — Word Search (LC 79)
# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# A B C E
# S F C S
# A D E E

# word = ABCCED
# Answer: True.

# what qualifies as a word
# so we are trying to match a word in an existing graph. The word can start from anywhere so we know that we need to iterate through all nodes
# we need a way to go left right up and down 
# and then also back track if the word does not match
# DFS Backtracking

# CHOICES: so the choices will be the surrounding characters 
# STATE: current row and column, what is the character we need to find, index of the word
# BASE CASE: found the word - so the last character is found and index is past the length of the word
# INVALID / PRUNING CASE: 
    # if the row column exceed the map size
    # letter is not found 
    # wrong character 
# CHOOSE: start with 0,0, index = 0 [A] and mark as temporarily marked
# EXPLORE: left right up and down in the dfs for next character
# UNDO: if not found restore it

def wordsearch(map, word):
    rowL = len(map)
    colL = len(map[0])

    def dfs(r,c,i):
        if(i == len(word)):
            return True
        if (
            r<0 or r>=rowL or 
            c<0 or c>=colL or
            map[r][c] != word[i]
        ):
            return False
        temp = map[r][c]
        map[r][c] = "#"

        found = (
            dfs(r+1,c, i+1) or 
            dfs(r,c+1, i+1) or 
            dfs(r-1,c, i+1) or 
            dfs(r,c-1, i+1) 
        )
        map[r][c] = temp
        return found
    
    for i in range (0,rowL):
        for j in range (0,colL):
            if (dfs(i,j,0)):
                return (True)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(wordsearch(board,word))