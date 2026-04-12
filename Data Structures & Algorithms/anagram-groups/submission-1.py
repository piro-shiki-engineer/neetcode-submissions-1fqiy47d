from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # for this edge case

        for s in strs:
            count = [0] * 26 # number of a-z
            
            for c in s:
                count[ord(c) - ord("a")] += 1 # a = 80, b=81
            
            result[tuple(count)].append(s)
        return result.values()
     