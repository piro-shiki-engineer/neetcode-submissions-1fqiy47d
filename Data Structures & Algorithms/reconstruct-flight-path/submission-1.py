class Solution:
    """
    Task: reconstruct the flight path departed from "JFK"
    
    In this problem, we gotta handling directed graph.
    So first, we need to construct graph, key is the name of airport.
    the velue is the list and this element is airport connected directly.
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        preMap = {}
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