class Solution:
    """
    Task: Return the longest palindromic substring

    I wonder if empty string is palicdromic? → palindromic, but empty string is impossible, 
    beacasu the length of input word is greater or equal to 1

    So, lets more clarify this problem by using Example 1
    Example 1
    Input: s = "ababd" Output: "bab"

    How to judge the word is palindromic. the answer is using two pointer like left and right pointer.
    We can express substring by usning start index and last index.
    I want make table coulmun is
    start index which is 0 to the length of given word,
    row is last index which 0 to the length of given word
    """
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s[i:j+1]) and len(res) < j - i + 1:
                    res = s[i:j+1]

        return res

    def isPalindrome(self, s: str):
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        