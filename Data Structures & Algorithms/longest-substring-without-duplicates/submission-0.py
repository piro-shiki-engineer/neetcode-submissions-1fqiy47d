class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        連続部分文字列
        Two Pointers の要素:
        l (left pointer)とr (right pointer)の2つのポインタを使用
        この2つのポインタは配列内の異なる位置を指し、条件に応じて移動
        ポインタ間の要素を評価対象とする

        Sliding Window の要素:
        ウィンドウの境界をlとrのポインタで定義
        重複文字が見つかった場合、左端(l)を進めてウィンドウを縮小
        新しい文字を見つけた場合、右端(r)を進めてウィンドウを拡大
        ウィンドウ内の要素をcharSetで管理

        実際の動作の例:
        Copys = "abcabcbb"
                        window
        iteration 1:     [a]          l=0, r=0
        iteration 2:     [ab]         l=0, r=1
        iteration 3:     [abc]        l=0, r=2
        iteration 4:     [bca]        l=1, r=3  # aが重複したのでlを移動
        """

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # 重複が無くなるまで
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res            
        
    def BruteFroce_lengthOfLongestSubstring(self, s: str) -> int:
        """
        BruteForceの解答
        ある文字から連続文字列を全て洗い出す
        →この時に集合演算子を用いて重複した場合にはその処理を抜け次の文字をスタートへ移動する
        """
        res = 0
        n = len(s)

        for i in range(n):
            charSet = set()

            for j in range(i, n):
                if s[j] in charSet:                    
                    break
                charSet.add(s[j])

            res = max(res, len(charSet))

        return res