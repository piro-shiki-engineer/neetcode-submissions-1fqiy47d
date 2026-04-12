"""
最初のアルファベット26文字をどう管理するか
prefix: 接頭辞
Trie:
効率よく文字情報を管理できるデータ構造

例えばappleを挿入しているとする。
この時appleの有無を検索し存在の有無を確認することができる。
またappを接頭辞prefixとして持つ単語を調べて時にもappleが返却される
単語の終了文字として記録しなければ登録した単語なのかそうでないのかが判定することができない
特定のprefixを持つかの記録だけであれば単語の終了字かは記録不要
複数の単語を記録する時に効率的であるすでにあるprefixから記録するだけでよくSpaceComplexityがよい
各深さの文字数はlowercaseのみであると最大26
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            # if charcter in cur.children, just move to the Node
            cur = cur.children[c]
        cur.endofWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            # if charcter in cur.children, just move to the Node
            cur = cur.children[c]
        return cur.endofWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            # if charcter in cur.children, just move to the Node
            cur = cur.children[c]
        return True
        
        