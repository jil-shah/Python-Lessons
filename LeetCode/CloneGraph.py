# # Problem 3 — Clone Graph
# # LeetCode 133 — Medium

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# start at node 1, create the node map original to new 
# traverse through each connected node, create a new node if it doesnt exist in the dictionary 
# 

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

def CloneGraph(current):
    if not current:
        return None

    #cloned for original -> clone
    clones = {}
    #create the recussion function 
    def dfs(node):
        if node in clones:
            return clones[node]
        # if it doesnt exist we need traverse the neighbors and create a new node
        copy = Node(node.val)
        clones[node] = copy
        for i in node.neighbors:
            copy.neighbors.append(dfs(i))
        return copy
    return dfs(current)

# O(V+E) Because of rescursion
# O(V)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned = CloneGraph(node1)

print(cloned.val)
print([n.val for n in cloned.neighbors])
    # Expected: [2, 4]