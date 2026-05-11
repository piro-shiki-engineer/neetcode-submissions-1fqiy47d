class Solution:
    """
    Task: Return true if the input s is macthed p while completing the conditions.

    CODITIONS: Meaning
    ".": matches any single chars
    "*": mathces 0 or more of preceding element.
    "c": Need to match exactly charcter "c".

    My IDEA: Checking all patterns depending on p's each elements. by using backtraking

    Case1. s = aa, b = .b 

    Eng: Jap
    preceeding: 前の
    """
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = {}

        def dfs(i, j) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (
                    dfs(i, j + 2) or           # unuse * 
                    (match and dfs(i + 1, j))  # use *
                )
                return dp[(i, j)]
            
            if match:
                dp[(i, j)] = (dfs(i + 1, j + 1))
                return dp[(i, j)]
            
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
        