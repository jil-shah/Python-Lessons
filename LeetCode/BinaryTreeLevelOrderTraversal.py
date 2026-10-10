# Problem 6 --- Binary Tree Level Order Traversal
# LeetCode 102 --- Medium

# Given:

#         3
#        / \
#       9   20
#          /  \
#         15   7
# Return:

# [
#     [3],
#     [9, 20],
#     [15, 7]
# ]

# traverse each row and then move down the tree 
# this indicates BFS - level order
# BFS requires a queue
# for row 1, node will start at 3, then we add to the queue. Length of queue = 1, we iterate through the queue, and pop, and add the value to temp resul
# then we add left and right to the queue. Since only one element, add the [3] to the result list
# get the length of the queue, iterate through it, pop left, add the value to the temp list. add any children to the queue
# go to 20 and repeat
from collections import deque
class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def BTLevelOrderTraversal(node):
    if not node: 
        return None
    
    results = []
    q = deque([node])
    while(q):
        tempR = []
        lenQ = len(q)
        for i in range(lenQ):
            n = q.popleft()
            tempR.append(n.val)
            
            if (n.left):
                q.append(n.left)
            if (n.right):
                q.append(n.right)
        results.append(tempR)

    return results

# Time: O(n)
# Space: O(n) worst case.


tree = TreeNode(1)

tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree.right.right = TreeNode(6)

print(BTLevelOrderTraversal(tree))
