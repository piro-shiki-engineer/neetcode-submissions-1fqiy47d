class Solution:
    """
    Task: Return minimum number of words in transformation sequence

    制約：1文字ずつしかTransformしていけない

    隣接リストは単語のそれぞれの位置を任意文字としする時にそれぞれがパターン化できる
    例：catのなどの3文字の場合→ ["*at", "c*t", "ca*"]

    パターン化された文字がキーとなって、それぞれの単語に該当する単語は隣接ノードになる
    キーは何文字目を任意とした

    "number of words in the shortest transformation sequence" --> Shortest path usually means BFS
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        n, m = len(wordList), len(beginWord)
        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(m):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0 # Not exist transform seaquence