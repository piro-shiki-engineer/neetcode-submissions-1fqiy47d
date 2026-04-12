class Solution:
    """
    Task: counting how many ways to decode a messages

    1012 → 012 or 12 (remove 1 string or 2 string.)
    
    012 
    is invalid string because first of this string is 0,
    and it's not following given mapping. return 0.

    12 → 2 or '' 
    2 → '' remove At this we cannot remove 2 string, because the length of string is less than 2.
    '' empty string, theres is a way to decode message, so count up and return 1. basecase.
    '' empty string, theres is a way to decode message, so count up and return 1. basecase.

    Bubble up the clidren result to parent and added all result.
    
    Compelxity:
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    N is the length of input string.

    We can 
    """
    def numDecodings(self, s: str) -> int:
        def dfs(s, memo = {}) -> int:
            if s in memo: return memo[s]
            if len(s) == 0: return 1

            result = 0
            if int(s[0]) != 0:
                result += dfs(s[1:], memo)
            
            if (len(s) >= 2 and
                (int(s[0]) == 1 or (int(s[0]) == 2 and int(s[1]) <= 6))
                ):
                result += dfs(s[2:], memo)

            memo[s] = result
            return result
        return dfs(s)
        