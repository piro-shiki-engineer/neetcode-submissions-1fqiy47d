class Solution:
    """
    Task: Get cheapest price from src to dst we can make in K steps

    From this problem context,
    there are 0 to n-1 nodes and which have each price(weight).

    Let me clarify this problem by using example 1.
    
    Why I cant solve this ?
    - 
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Dijsktra法での実行可能であるがより"at most k stops"という条件を活かしきれていない
        → Bellman Ford法

        Negative Weightを活用できることが利点ことが特徴として再現→負の閉路を見つけることができる
        負の閉路とは、その閉路の和の合計が負の時負の無限大に飛んでしまう閉路である

        BFSを実行するときにそれぞれのノードからの最小プライスを伝搬することが可能になる
        Time: O（EV）but, in this case O(Ek)
        E is the number of edges 
        V is the number of nodes
        k is the max stops you can

        tempPricesとはsrcから見たときの各層時点での最小コストである（ただし問題の表現上k+1層まで見ることになる）
        →k+1層までみないとdstに到達可能な場合であっても到達できない
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices

        return prices[dst] if prices[dst] != float("inf") else -1


    def findCheapestPrice_dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        優先度付きキュー（抽象的な概念）
        「優先度の高いものから取り出せるキュー」
        ↓
        これを実現するために
        ↓
        ヒープ（具体的なデータ構造）を利用して実装

        heapify or (heapush and heappop) 実装基準基準のフローチャート
        全データが最初から揃っている？
        ├─ YES → heapify を使う（O(N)） → 例: 配列をheapに変換
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
        
        adj = defaultdict(dict)
        for from_node, to_node, price in flights:
            adj[from_node][to_node] = price
        
        minHeap = [(0, 0, src)] # (totalPrice, totalStep, current_node)
        
        while minHeap:
            totalPrice, totalStep, curr = heapq.heappop(minHeap)
        
            if curr == dst: # reach to dst
                return totalPrice
            
            if totalStep > k: # over max step k
                continue
            
            for nxt, price in adj[curr].items():
                heapq.heappush(minHeap, (totalPrice + price, totalStep + 1, nxt))
        
        return -1