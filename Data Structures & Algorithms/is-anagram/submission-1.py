class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram は 循環文字列

        # ソートした文字列が同じならanagram
       s_ = sorted(list(s))
       t_ = sorted(list(t))
       
       return ''.join(s_) == ''.join(t_)
        