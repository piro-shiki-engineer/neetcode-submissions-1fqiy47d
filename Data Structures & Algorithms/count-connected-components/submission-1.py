class Solution:
    """
    Task: Count up the connected components in that graph
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        result = 0
        def dfs(node):
            if node in visit:
                return 0

            visit.add(node)
            for neighbor in adj[node]:
                if node == neighbor:
                    continue
                dfs(neighbor)
            
            return 1
            
        for node in range(n):
            if not node in visit:
                result += dfs(node)

        return result
