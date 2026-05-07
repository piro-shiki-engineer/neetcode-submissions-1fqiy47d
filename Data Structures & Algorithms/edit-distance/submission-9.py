class Solution:
    """
    Task: Get the minimum number of operations make word1 eqaul to word2

    First, we need to find the position that the character are diffrent between word1 and word2

    Next, we need to make descition from 3 options.
    1) Insert correct one char
    2) Delete the one char
    3) Replace one char from uncorrect to correct

    BruteForces like dfs
    Let me descirbe some examples for clarifing this problem.
    I gonna use example 1.

    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i][j + 1],
                        dp[i + 1][j + 1]
                    )
        return dp[0][0]

    def minDistance_optimedTopDownDP(self, word1: str, word2: str) -> int:
        """
        Optimized Top Down DP
        Time: O(n * m)
        Space: O(n * m)
        """
        memo = {}
        m, n = len(word1), len(word2)
        def dfs(i, j):
            if i == m:
                return n - j
            
            if j == n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(
                    dfs(i + 1, j + 1), # replace
                    dfs(i, j + 1), # insert
                    dfs(i + 1, j) # delete
                )
            return memo[(i, j)]
        return dfs(0, 0)

    def minDistance_unefficient(self, word1: str, word2: str) -> int:
        """
        m is the length of word1
        n is the length of word2

        Time: O(mn * (m + n)) -> O(m * n^ 2) 
        Space: O(mn * (m + n)) -> O(m * n^ 2)

        m + nの部分は今回コードのword1 と word2の残りの文字列コピーにより発生している
        →そのためよりよいのは、ポインターのみを保持して管理すると余分なメモリや時間は発生しない
        """
        memo = {}
        # m, n = len(word1), len(word2)
        def dfs(w1, w2):
            # both w1 and w2 is empty string
            if w1 == "" and w2 == "":
                return 0

            # either w1 or w2 is empty string
            if w1 == "" and w2:
                memo[(w1, w2)] = len(w2)
                return len(w2) # 残りをinsert
            
            if w2 == "" and w1:
                memo[(w1, w2)] = len(w1)
                return len(w1) # 残りをdeletet
            
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            
            if w1[0] == w2[0]:
                memo[(w1, w2)] = dfs(w1[1:], w2[1:])
            else:
                memo[(w1, w2)] = 1 + min(
                    dfs(w1, w2[1:]),      # insert
                    dfs(w1[1:], w2),      # delete
                    dfs(w1[1:], w2[1:])   # replace
                )
            return memo[(w1, w2)]

        return dfs(word1, word2)