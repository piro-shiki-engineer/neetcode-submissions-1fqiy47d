"""
グリッド内でひとつセルを移動すると比較するTrieの深さが変化する
"""

class TrieNode:
    def __init__(self):
        self.children = {} # "a": TrieNode
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self # オブジェクト自身
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        visit = set()
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        ROWS, COLS = len(board),len(board[0])

        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children) :
                return 

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r  in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
            
        return list(res)