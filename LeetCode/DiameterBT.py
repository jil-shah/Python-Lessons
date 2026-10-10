# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
#      1
#   2     3 
# 4   5
# ans: 3

# problem: 
# we want to find the max diameter in the tree
# by the explaination what i think this means is the longest path that exists
# since it mentions that it can pass through the root 
# that simplifies the problem

# 1 + dfs(lt) + dfs(rt)
# so what we do is we want to find the max depth in the left subtree and then find max in the right subtree
# then the longest path by default will be that 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Test run 
#  node = 1  max = 0 
#   left: 2  max = 1
#     left: 4   max = 2
#   right:3 
# when we see left = none that is the max of a subtree
# explore until none is reached
def diameterBT(root):
    diameter = 0
    def dfs(node):
        if not node:
            return 0
        lt = dfs(node.left)
        rt = dfs(node.right)
        diameter = max(diameter,lt + rt)

        return 1 + max(lt,rt)
            
    dfs(root)
    return diameter


        