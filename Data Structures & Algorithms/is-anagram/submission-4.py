class Solution:
    """
    Retrun true if the two strings s and t are anagrams, not so return false
    
    compare soerted s and t
    Time: O(2nlogn) -> O(nlogn)
    Space: O(1)

    Sacrifice  a little extra memory

    First iterate through s for counting chars by using HashMap

    Second iterate through t for counting chars, but decreasing the number of occurance
    if there is 0 chars just return false, its not anagram

    We reach the end of the string t, that means two strings are anagrams.

    Time: O(2n) -> O(n)
    Space: O(n)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1

        for c in t:
            if count_s[c] == 0:
                return False
            
            count_s[c] -= 1
        
        return True
        