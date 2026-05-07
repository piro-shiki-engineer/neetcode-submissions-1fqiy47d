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
        