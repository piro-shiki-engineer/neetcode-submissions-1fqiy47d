class Solution:
    def alphaNum(self, c: str)-> bool:
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

    """
    Task: Return True if given string is palindrome, Return false if not so

    use characters in input to check:
    charcters: A-Z, a-z, 0-9

    remove the ohter: white space, special characters etc ?/
    Basically, We need to conver uppercase characters into small for chekcing palidorome.

    After converting, We gonna check if the string is palinedorome or not by using two pointer.

    left = 0, right = len(converted_string) - 1 and compare i-th chacters are or not utnil left index eqauls to right index.
    
    At this moment, I think I can check palidrome for One way that means we can convert and check at the same time.

    Time: 26
    """
    
    def isPalindrome(self, s: str) -> bool:
        def convert(s: str) -> str:
            if ord("a") <= ord(s) <= ord("z"):
                return s

            if ord("A") <= ord(s) <= ord("Z"):
                s = chr(ord(s) - ord("A") + ord("a"))
                return s

            if ord("0") <= ord(s) <= ord("9"):
                return s

            return ""

        left, right = 0, len(s) - 1
        # move to first target chacracters

        while left < right:
            while left < right and convert(s[left]) == "":
                    left += 1
            while left < right and convert(s[right]) == "":
                    right -= 1

            if left < right and convert(s[left]) != convert(s[right]):
                return False

            left += 1
            right -= 1

        return True

