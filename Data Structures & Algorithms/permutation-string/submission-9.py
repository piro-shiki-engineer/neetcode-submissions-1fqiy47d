from itertools import permutations

class Solution:
    """
    文字列s1に文字列s2の順列のどれかが含まれるかを判定する問題
    順列であっても配列番号的には連続である必要があることに注意

    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        問題文の最後にあるBoth strings only contain lowercase letters.
        →つまり取りうる値は小文字のアルファベット26種であること利用し、Space Complextity の改善する

        O(26N) that means O(N)

        The maximu size of HashMap is 26.

        We copmare two HashMap, then maches = 0 but updating to the number of mathce

        mathcesは、各単一のアルファベットの数が一致の合計になっている

        O(26) となる各地点からのmathces
        
        time 
        O(26): compare the the total number of signle alphabet s1 and s2.
        O(N) : S2の各地点からS1の長さ分のアルファベットの数の計測を行う総回数

        time complexity → O(26) + O(N) = O(N)

        """
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # 各スライドで変わるのは1文字ずつ（ここでは右端の追加）
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
            
            # 各スライドで変わるのは1文字ずつ（ここでは左端の削除）
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1

        return matches == 26
            
    
    def HashTable_checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}

        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        for i in range(len(s2)):
            count_s2, current = {}, 0
            need = len(s1)
            for j in range(i, len(s2)):
                count_s2[s2[j]] = count_s2.get(s2[j], 0) + 1
                if count_s1.get(s2[j], 0) < count_s2[s2[j]]:
                    break
                if count_s1.get(s2[j], 0) == count_s2[s2[j]]:
                    current -= 1
                
                if current == need:
                    return True

        return False

    def BuretForce_checkInclusion(self, s1: str, s2: str) -> bool:
        """
        BreteForce
        s1の全ての順列がs2に含まれているか判定する。
        itertoolsのpermutatins N!
        """
        if len(s1) > len(s2):
            return False

        patterns = ["".join(pattern) for pattern in permutations(s1)]
        window_size = len(s1)

        for pattern in patterns:
            left = 0
            while left <= len(s2) - window_size:
                right = left + window_size - 1
                current = s2[left:right+1] 
                if current == pattern:
                    return True
                
                left += 1
                    
        return False