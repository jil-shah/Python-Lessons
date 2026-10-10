# Problem 5 --- Validate Binary Search Tree
# LeetCode 98 --- Medium

# A BST follows:

# all values in left subtree < node
# all values in right subtree > node
# Example valid:
#         5
#        / \
#       3   8
# But here's the trap:
#         5
#        / \
#       3   8
#          /
#         4
# 4 < 8, so it looks locally okay.

# But 4 is in the right subtree of 5, so it must also be:

# > 5
# It isn't.

# Therefore the tree is invalid.

# check left < node or right> node is not sufficient
# there needs to be some kind of running list of allowed values
# left ( -inf to 5) right (5 to inf)
# each node will receive an accepted range. 

# 5 -> -inf to +inf
# RN -> -INF to 5 
# LN -> 5 to +INF

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def ValidateBST(node):

    def ValidAgainstRange(node, lowerBound, upperBound):
        if not node:
            return True
        
        if not (lowerBound < node.val < upperBound):
            return False
        
        return (
            ValidAgainstRange(node.left, lowerBound, node.val)
            and 
            ValidAgainstRange(node.right, node.val, upperBound)
        )

        
    return ValidAgainstRange(node, float("-inf"), float("inf"))

valid = TreeNode(2)
valid.left = TreeNode(1)
valid.right = TreeNode(3)
# Expected: True
print(ValidateBST(valid))

invalid = TreeNode(5)
invalid.left = TreeNode(6)
invalid.right = TreeNode(7)

print(ValidateBST(invalid))
# Expected: False