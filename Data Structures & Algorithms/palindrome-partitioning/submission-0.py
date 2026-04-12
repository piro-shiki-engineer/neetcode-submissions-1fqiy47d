class Solution:
    """
    BruteForece -> Backtraking
    We check if all subsring is palindrome
    """
    def partition(self, s: str) -> List[List[str]]:
        chars = list(s)
        print(chars)
        res = []

        def backtraking(i, cur):
            if i == len(s):
                res.append("".join(cur.copy()))
                return
                
            if cur[0] == cur[-1]:
                cur 

            # contain element
            cur.append(chars[i])
            backtraking(i + 1, cur)
            
            # not contain element
            backtraking(i + 1, cur)

            while i > len(cur) and cur[i] == i + 1:
                cur[i] += chars[i]
                i += 1
                

            backtraking(i, cur)
        
        backtraking(0, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1) # nextキャラクター
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True