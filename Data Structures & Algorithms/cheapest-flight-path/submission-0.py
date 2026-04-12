class Solution:
    """
    Task: Get cheapest price from src to dst we can make in K steps

    From this problem context,
    there are 0 to n-1 nodes and which have each price(weight).

    Let me clarify this problem by using example 1.
    
    優先度付きキュー（抽象的な概念）
    「優先度の高いものから取り出せるキュー」
    ↓
    これを実現するために
    ↓
    ヒープ（具体的なデータ構造）を利用して実装


    ## 判断基準のフローチャート
    全データが最初から揃っている？
    ├─ YES → heapify を使う（O(N)）
    │         例: 配列をheapに変換
    │
    └─ NO → データは動的に生成される？
        ├─ YES → heappush を使う（O(log H)）
        │         例: BFS, Dijkstra, リアルタイム処理
        │
        └─ バッチで追加できる？（10個以上まとめて）
            ├─ YES → append複数回 + heapify 1回を検討
            │         ※実務では稀、heappushの方が安全
            │
            └─ NO → heappush を使う
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for from_node, to_node, price in flights:
            adj[from_node].append((to_node, price))
        
        minHeap = [(0, 0, src)] # (totalPrice, totalStep, current_node)
        
        while minHeap:
            totalPrice, totalStep, curr = heapq.heappop(minHeap)
        
            if curr == dst: # reach to dst
                return totalPrice
            
            if totalStep > k: # over max step k
                continue
            
            for nxt, price in adj[curr]:
                heapq.heappush(minHeap, (totalPrice + price, totalStep + 1, nxt))
        
        return -1