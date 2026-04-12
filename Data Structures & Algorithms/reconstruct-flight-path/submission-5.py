class Solution:
    """
    Task: reconstruct the flight path departed from "JFK"
    
    In this problem, we gotta handling directed graph.
    So first, we need to construct graph, key is the name of airport.
    the velue is the list and this element is airport connected directly.

    Uhmn, I wannt to  use the heap for manage the neighbors sorted in dictionary order.
    
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Backtracking(DFS) approach
        Time: O(E * V) - worst case visits each edge V times due to backtracking
        Space: O(E) - adjacency list storage + recursion stack        """
        adj = collections.defaultdict(list)
        
        tickets.sort() # O(ElogE)
        for src, dist in tickets: # O(E)
            adj[src].append(dist)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = adj[src].copy()
            for i, v in enumerate(temp): # O(E)
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            
            return False

        dfs("JFK")
        return res

    def findItinerary_HierholzerRecursion(self, tickets: List[List[str]]) -> List[str]:
        preMap = {} # node: heapq[str] # next nodes key
        for src, dest in tickets:
            if src not in preMap:
                preMap[src] = []
            
            heapq.heappush(preMap[src], dest) # sorted lexicographically order 

        path = []
        def dfs(src):
            while (src in preMap and preMap[src]):
                dst = heapq.heappop(preMap[src])
                dfs(dst)
            path.append(src)

        dfs("JFK")            

        return path[::-1]