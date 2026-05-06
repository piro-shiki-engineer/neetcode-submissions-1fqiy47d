class Solution:
    """
    Task: Return the number of distinct subsequences of s which are equal to t

    英：和
    distinct: 異なる

    Fisrt: BruteForce

    We want to know the all subsuquences of s.
    So, I gonna use discition tree.
    There are 2 options like use or unuse i-th value of s.

    Let me describe some examples for clarifing this sols and this prolbem.
    """
    def numDistinct_DFS(self, s: str, t: str) -> int:
        """
        Complexity:
        Time: O(m * 2^n)
        Space: O(nm) # 各呼び出しで現在の文字列を保持しているため

        n is the length of s. m is the length of t
        """
        def dfs(i, curr):            
            if len(curr) == len(t):
                return 1 if curr == t else 0
            
            if i == len(s):
                return 0
            
            return dfs(i + 1, curr + s[i]) + dfs(i + 1, curr)
        return dfs(0, "")

    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            if len(curr) == len(t):
                return 1 if curr == t else 0
            
            if i == len(s):
                return 0
            
            memo[(i, curr)] = dfs(i + 1, curr + s[i]) + dfs(i + 1, curr)
            return memo[(i, curr)]
        return dfs(0, "")