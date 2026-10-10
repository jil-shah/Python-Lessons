# Problem 4 --- Invert Binary Tree
# LeetCode 226 --- Easy

# Before:
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9
# After:
#         4
#        / \
#       7   2
#      / \ / \
#     9  6 3  1

# every child siblings is switched
# left child ↔ right child
# swap the children, and then recurssively swap each subtree

#O(N) for both, recurvsive and all we need to is iterate through each node once
from collections import deque
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val=val
        self.left=left
        self.right=right

def InvertBT(root):
    if not root:
        return None

    root.left,root.right = root.right, root.left
    InvertBT(root.left)
    InvertBT(root.right)

    return root

def print_tree(root):
    if not root:
        print([])
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    print(result)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print_tree(InvertBT(root))  # Expected: 3

# Test 3: empty tree
print_tree(InvertBT(None))  # Expected: 0

