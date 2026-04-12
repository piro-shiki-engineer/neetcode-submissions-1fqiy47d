class Solution:
    ''' 
    tips
    エンコード：配列の各要素にある文字列を1つの文字列に変換
    デコード：与えられた文字列から単語ごとに切り分け切りわける
    そのまま足してしまうとどこで区切られいたかはわからないため、単語の始まりと終わりを表す記号で決める
    文字数と区切り文字列の組み合わせて表現
    →仮に区切り文字として設定した記号が含まれても問題ない
    '''
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # 初めに iからj-1の要素であるから一つの文字にアクセス
            i = j + 1
            j = i + length
            res.append(s[i:j])
            
            i = j
                
        return res
