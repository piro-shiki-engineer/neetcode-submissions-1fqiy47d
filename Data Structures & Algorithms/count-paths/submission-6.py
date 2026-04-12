class Solution:
    """
    Task: Count the unique paths from left-top right to right-bottom

    start(0, 0) goal(m-1, n-1)


    """
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Bottom Up DP
        右下のゴール単体でみると生き方は一通りである。
        また、右下から左上に評価うするとより効率的に行える。
        また、行単位で左に評価することで、2列分だけの空間計算量に抑えられる
        """

        row = [1] * n

        for i in range(m - 1): # 最下行は自明であるため
            newRow = [1] * n
            for j in range(n - 2, -1, -1): # from right - 1 to right because rightest cell is denitely 1
                newRow[j] = newRow[j + 1] + row[j]
            
            row = newRow
        
        return row[0]


    def uniquePaths_TopDown(self, m: int, n: int) -> int:
        """
        startから順に右・下と移動する
        
        Early Return
        ゴールに辿り着けば1、境界を超えた場合には0を返す
        もしくはすでに訪問済みの場合は結果のみを返す。
        """
        memo = {} # key: (x, y), value: unique path from (x, y) to (m - 1, n - 1)
        def dfs(x: int, y: int) -> int:            
            if (x, y) in memo:
                return  memo[(x, y)]
            
            if x >= m or y >= n:
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1

            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)

            return memo[(x, y)]
                
        return dfs(0, 0)