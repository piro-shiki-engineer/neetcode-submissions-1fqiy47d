import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        自分で考えた方針：
        与えられた文字列から空白や記号を取り除く
        一つの文字列が回文であるかの判定
        各単語に大文字が含まれているならばいるならば、小文字に変換する
        '''
        splitWords = list(map(str, s.split()))
        joinedStr = ""
        for word in splitWords:
            word = "".join([word[i] for i in range(len(word)) if word[i].isalnum()])
            joinedStr += word.lower()
        print(joinedStr)
        return joinedStr == joinedStr[::-1]