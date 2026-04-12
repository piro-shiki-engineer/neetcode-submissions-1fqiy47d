class Solution:
    """
    You are given a string s consisting of only uppercase english characters and an integer k.
    You can choose up to k characters of the string（最大K個の文字列の文字） and replace them with any other uppercase English character.
    一つの文字で構成される連続部分文字列の最大
    具体例を考える

    Input: s = "XYXZ", k = 2

    部分文字列の最大長を計測にはSliding Windowを使う
    
    """

    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding Window (more efficiently )
        this algo is more efficiently than SlidingWindow_characterReplacemen ,like this O(26*N) → O(N) in actually
        """
        res = 0
        count = {}

        left = 0
        max_frequency = 0
        
        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:   # （iからjまでの文字列の長さ）と（最も頻度多い文字の頻度）との差がkになるように減らす処理
                count[s[left]] -= 1
                left += 1
                    
            res = max(res, right - left + 1)
        
        return res

    def SlidingWindow_characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding Window

        Time Complexity : O(N^M) N is the length of input string s
        → Maximum number of M is 26, so Time Complexity is O(26 * N)→ O（N）
        Space Complexity : O(M)


        """
        res = 0
        charSet = set(s)

        for char in charset:
            count = left = 0

            for right in range(len(s)):
                if char == s[rihgt]:
                    count += 1

                while (right - left + 1) > k:
                    if char == s[left]:
                        count 
                    left += 1
                
                if (j - i + 1) - max_frequency <= k:  # （iからjまでの文字列の長さ）と（最も頻度多い文字の頻度）との差がk以下
                    res = max(res, j - i + 1)
        
        return res


    def BruteForce_characterReplacement(self, s: str, k: int) -> int:
        """
        BruteForce
        1. 文字列内にアルファベットを全てチェックする　"XYXZ"　→ {"X", "Y", "Z"}
        2. 与えられた文字列の全ての箇所を2文字で置き換えて、一つの文字で構成される部分文字列の最大長を計測する
        Time Complexity : O(N^2)
        Space Complexity : O(M)
        """
        res = 0

        for i in range(len(s)):
            count, max_frequency = {}, 0

            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_frequency = max(max_frequency, count[s[j]])
                
                if (j - i + 1) - max_frequency <= k:  # （iからjまでの文字列の長さ）と（最も頻度多い文字の頻度）との差がk以下
                    res = max(res, j - i + 1)
        
        return res

        