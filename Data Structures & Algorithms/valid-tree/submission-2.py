class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

class Solution:
    """
    Task: check whether these edeges make up a valid tree

    Strict:
    There are no duplicates edges like [0, 1] and [1, 0]. 

    I think tree has properties like
    - A node has one undirected edge like 0 <-> 1
    - there is 

    I want to calrify this problem, so let me describe by using the examples.

    A path between any node and the node is only one way. In other words, there is no cycle

    Cycle Detection
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        def dfs(node, pre):
            if node in visit:
                return False
            
            visit.add(node) # 一度訪れた場合には隣接ノードから他ノードは辿れるはず
            for neb in adjList[node]:
                if neb == pre:
                    continue
                if dfs(neb, node) == False:
                    return False

            return True
        
        return dfs(0, -1) and len(visit) == n # 後ろの条件は一つの木かを確認してる
