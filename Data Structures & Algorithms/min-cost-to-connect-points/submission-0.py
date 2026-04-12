class Solution:
    """
    Task: Get the minimum operations to conect all points

    In this problem also say the one point is conected to only one node.
    
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        res = 0
        visit = set()
        minHeap = [[0, 0]]

        while len(visit) < n:
            cost_i, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            
            res += cost_i
            visit.add(i)
            for cost_j, j in adj[i]:
                heapq.heappush(minHeap, [cost_j, j]) # 単純な接続操作のみであるためcostは加算しない

        return res
                

        
        