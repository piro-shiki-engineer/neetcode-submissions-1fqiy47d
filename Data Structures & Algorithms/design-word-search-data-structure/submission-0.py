class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def backtrack(index, node):
            # ベースケース
            if index == len(word):
                return node.endOfWord
            
            char = word[index]
            
            if char == '.':
                # 全ての選択肢を試す（バックトラッキング）
                for c in node.children:
                    if backtrack(index + 1, node.children[c]):  # 選択
                        return True
                    # 自動的にバックトラック（return後、次のcを試す）
                return False
            else:
                # 通常の1つの選択肢
                if char in node.children:
                    return backtrack(index + 1, node.children[char])
                return False
        return backtrack(0, self.root)