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
     
class Solution:
    """
    Task: Return List and the elment is also list, sublist contains anagrams.

    Anagram is a string contains same character, but its allow string to follow any order.
    To make anagram group, we need to judge if the string is anagram of the order.

    Think more simply, we need judge two strings are angaram for each other.

    Its simple sorted for asdeding order and join as new strings
    And compare the two new strings. if it's same, two strings are anagram.

    So, I want use dictionary for storing the anagram grop. key is ascdign ordered strings. and value is List of Anagram Group

    Lets think example1.
    Input: strs = ["act","pots","tops","cat","stop","hat"] Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    Convert each element from str into List[str] ex. "act" → [a, c, t]
    So, Convert input is like this [[a, c, ,t], [p, o, t, s], [c,a,t],[s,t,o,p][h, a, t]

    Dictionary = {}

    Time Compelxity: O(n * mlogm) n is the length of strs. m is the length of longest str in strs.
    Space: O(n)

    Optimize:
    Bottle neck is the part of judging where the elment belong to the angaram Group O(mlogm)
    Actually we dont need to use sort algo. just make a array the length 26 because the total number of smaller characters is 26.
    i = 0 a, i = 25 is  count up each characeters. and store in dict key is tupled 26 list and value is list of anagram

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} # key: sorted strings value: List[anagram]

        for word in strs:
            # chrs = list(word)
            # chrs.sort() # O(mlogm)
            # sorted_word = "".join(chrs)

            # if sorted_word not in hashMap:
            #     hashMap[sorted_word] = [word]
            # else:
            #     hashMap[sorted_word].append(word)


            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1

            if tuple(count) not in hashMap:
                hashMap[tuple(count)] = [word]
            else:
                hashMap[tuple(count)].append(word)


        return [anagramGroup for anagramGroup in hashMap.values()]
            
