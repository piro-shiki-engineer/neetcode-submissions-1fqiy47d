class Solution:
    """
    Task: Grouping words, each elments in a group are anagarms

    Time: O(n * m) n is the length of the input array stsr, and m is the longest length of the word
    Space: O(n * m)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        cntChars = [[0] * 26 ] * len(strs)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())
        

