# 236. Lowest Common Ancestor of a Binary Tree
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary tree, 
# find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the 
# lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Problem: we want to know the common ancestor between two nodes
# Find the lowest node whose subtree contains BOTH p and q.

# Example 
# 5,1 
# 3 -> left subtree 
# 5 is found [3]
# now we need to search for 1, its in the right subtree [3]

# 3 -> 5,4 
# left subtree we found 5 found p 
# check left subtree -> 6 -> null
# check right subtree -> 2
    # check left 7 -> null 
    # check right 4 - found q [3,5] [3,5,2,4]
# the problem with this is solution 1, it suggests we would need to loop through twice 
# O(n^2)

# each subtree can tell us:
    # found p
    # found q
    # found none
    # already resolved 
#this can be the smaller problem did left find anything 
# did right find anything 

# if both found then the current node is the LCA
# BASE CASE: root is none -> none, root is found -> root

class ListNode:
    def __init__(self, val,left, right):
        self.val=val
        self.left = left
        self.right = right

def Lca(root, p,q):
    if not root:
        return None
    if (root.val == p or root.val == q):
        return root

    left = Lca(root.left,p,q)
    right = Lca(root.right,p,q)

    if(left and right):
        return root

    if (left):
        return left

    return right

  