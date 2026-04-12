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
        component = set()
        result = 0
        def dfs(node):
            if node in visit:
                return 0
            
            if node in component:
                return 1

            component.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            
            component.remove(node)
            visit.add(node)
            return 1
            
        for node in range(n):
            result += dfs(node)

        return result

