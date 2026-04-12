class Solution:
    def countSubstrings(self, s: str) -> int:
        unique_palindromes = set()
        n = len(s)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or (i + 1, j - 1) in unique_palindromes):
                    unique_palindromes.add((i, j))

        return len(unique_palindromes)


