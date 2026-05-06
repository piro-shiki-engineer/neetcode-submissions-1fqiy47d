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