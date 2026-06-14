class Solution:
    """
    Task: Return a list of integer representing the size of substring in order they appear in the string.

    - Split given string into as many substring as possible
    - Ensure that each letter appears in at most one subsring

    To Make problem context clarify, Shall we think some examples.

    Time Compexity: O(n)
    Space Complexity: O(m)

    m is the total number of unique characters in given string.
    """
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        res = []
        start = last = 0
        for i in range(len(s)):
            last = max(last, lastIndex[s[i]])

            if i == last:
                res.append(last - start + 1)
                start = i + 1
            
        return res
        