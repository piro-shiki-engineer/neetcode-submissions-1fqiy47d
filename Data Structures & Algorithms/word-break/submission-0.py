class Solution:
    """
    Task: Check if it is possible to construct s by using words in dictionary.
    limit: we can use one word as many as need, not one time.
    In this problem, return ture becauese s can be split into small words.
    In other words, return true if it's possible to construct given s by concatenating words in given wordDict.

    I want to use descition tree. edge means the word is a part of target s.
    In other words, the word is prefix of s, and the next node that is a suffix is next target node.
    And, Return ture if target string is empty string that means we can construct input string "s" by using the string element of the given wordDict.
    And Retrun false if the word in wordDict is not prefix.

    As you can see, there are duplicates tree.
    So, I want to store the result and reuse by using memoization.

    Time: O(N*M(*M) M is The length of input sring s, and N is the is length of input array.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def isPrefix(s, word):
            if len(word) > len(s):
                return False
            
            return s[:len(word)] == word

        def dfs(s: str, wordDict: List[str], memo: Dict[str, bool]) -> bool:
            if s in memo:
                return memo[s]
            if s == '':
                return True

            for word in wordDict:
                if not isPrefix(s, word):
                    continue
                
                if dfs(s[len(word):], wordDict, memo):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        return dfs(s, wordDict, {})

        