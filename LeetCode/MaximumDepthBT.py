# Problem 3 --- Maximum Depth of Binary Tree
# LeetCode 104 --- Easy

#         3
#        / \
#       9   20
#          /  \
#         15   7

# Maximum depth:
# 3

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

# use dfs and a counter.
# start at 1, and then we want the max of each subtree 1+ max(left,right)

# base case: if empty tree; ans = 0
# solve each subtree and then combine the answers
# recursive patten for each subtree and then combine the answers 

def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1+max(left, right)

# Time = 0(N) you visit each node only once 
# space = O(h) the height of the tree 

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))  # Expected: 3

# Test 2: one node
single = TreeNode(1)
print(maxDepth(single))  # Expected: 1

# Test 3: empty tree
print(maxDepth(None))  # Expected: 0

# Test 4: unbalanced tree
deep = TreeNode(1)
deep.left = TreeNode(2)
deep.left.left = TreeNode(3)
deep.left.left.left = TreeNode(4)

print(maxDepth(deep))  # Expected: 4