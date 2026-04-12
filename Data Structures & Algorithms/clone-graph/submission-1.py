"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    Task:
    - deep copy undirected graph from adjaency list
    - Any element of adjaency list is meaning that this element conectet to this one node.

    Ex1)
    Input: adjList = [[2],[1,3],[2]]

    From this input, we can know that the number of all nodes in graph is 3.
    [1] -> [2]
    [2] -> [1, 3]
    [3] -> [2]

    the number of nodes → length of adjacency list → 3
    Actually, we dont need to care about 
    Next, I want to write down as pseudo code

    steps)
    1. determin index as i(in python 0 based index)
    2. make Node object which values is i+1 and the neighbors is adjList[i]
    3. Until end of adjList, repeat step 1 and step.


    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)

        queue = deque([node])

        while queue:
            cur = queue.popleft()

            for nei in cur.neighbors: # Travaserl current node's adjcent node
                if not nei in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])
            
        return oldToNew[node]
