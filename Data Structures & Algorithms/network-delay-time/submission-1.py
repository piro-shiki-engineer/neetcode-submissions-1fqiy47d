class Solution:
    """
    Task: Return minmum time to visit all nodes from k

    I gonna make the graph by using adjcency matrix
    
    Why I cant solve ?
    - 
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        visit = set()
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1
            for n2,  w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + time, n2))
            
        return time if len(visit) == n else -1



        