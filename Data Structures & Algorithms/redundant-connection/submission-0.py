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

    # def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
    #     n = len(edges)
    #     adjList = [ [] for i in range(n + 1)]
        
    #     for u, v in edges:
    #         adjList[u].append(v)
    #         adjList[v].append(u)
        
    #     result = None
    #     def dfs(node, prev):
    #         nonlocal result
    #         if node in visit: # detect the cycle
    #             result = [node, prev]
    #             return
            
    #         visit.add(node)
    #         for neighbor in adjList[node]:
    #             if neighbor == prev:
    #                 continue
    #             dfs(neighbor, node)
    #         return

    #     for i in range(1, n):
    #         visit = set()
    #         dfs(1, -1)
    #         res = 
        
    #     return result