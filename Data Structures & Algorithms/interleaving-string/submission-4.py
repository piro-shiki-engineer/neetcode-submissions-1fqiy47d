class Solution:
    """
    Task: Check if s3 is formed by interleaving s1 and s2 together

    What is interleabving s and t si done by s and t.

    Diving s and t into n and sustring following coditinos:
    n is the number of s's substrings,
    m is the number of t's substrings

    abs(n - m) <= 1

    First thing we should know or manage is the substrings of s and t

    We need to make decsition to take char from s1 or s2.

    英語：日本語
    Interleave : 
    relative order: 相対順序
    arbitrary: 任意の
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False for j in range(n + 1)]  for i in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
    
    def isInterleave_topDown(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True

            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            memo[(i, j)] = False            
            return False
        
        return dfs(0, 0)