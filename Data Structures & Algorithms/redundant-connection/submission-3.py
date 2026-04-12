class Solution:
    """
    Task: Return one edge that The graph can be converetd into no cyclical graph

    We should detect cycle and cut off edge ,
    which is conected highest rank node in graph.

    Strict
    - There are no repeated edges and no self-loops.

    So let me clarify this problem by desribing the examples.

    Why I cant solve ?
    - I should return the output edge from input's edges not adjList
    
    学んだこと
    - Tree性質としてノード数はエッジ数+1となる。
    - Cycle Detection 問題ではまず初めにDFS+Hashsetを検討し、難しければUnionFindを戦略的に選択
    - UnionFindではノード間が接続されているかを共通rootから瞬時に判断することができる。
    - UnionFindeで扱えるのはundireted graphのみ,なぜならCommon Ancestorのみを基本的に管理し、厳密なノード間の関係は管理されない
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)] # i th node -> parent, initially its self 
        rank = [1] * (n + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

    def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        cycle = set()
        cycle_start = -1
        
        def dfs(node, parent):
            nonlocal cycle_start
            if node in visit:  # サイクル検出
                cycle_start = node
                return
            
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                if cycle != -1:
                    cycle.add(node)
                if node == cycle_start:
                    cycle_start = -1
                    return
        
        dfs(1, -1)
        
        # edgesの逆順でサイクル内エッジを探す
        for u, v in reversed(edges): # return the edge that appears last in the input edges.
            if u in cycle_nodes and v in cycle_nodes: 
                return [u, v]
        
        return []