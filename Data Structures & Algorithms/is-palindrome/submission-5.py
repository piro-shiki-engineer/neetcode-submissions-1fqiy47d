import re

class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        '''
        自分で考えた方針：
        与えられた文字列から空白や記号を取り除く
        一つの文字列が回文であるかの判定
        各単語に大文字が含まれているならばいるならば、小文字に変換する
        alphanumeric とはa-z、A-Zそして数字→半角英数字（記号を除く）

        isalnum()を使うとメモリを使ってしまう。→自分で実装するとよい文字コードを利用する
        最適解は左と右からそれぞれ比較していき中央で終わるのかを確認すればよい
        空白や特殊記号を参照したときは何もせずにインクリメントする
        '''
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
