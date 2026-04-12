class Solution:
    """
    Task:
    Derive the order based on the given non empty list words,
    which is sorted on this new language

    if the string fullfil the all conditions below, it means th
        1. the first letter where they differ is samller in a than b
        2. a is a prefix of b and a.length < b.length
        → both a and b has the same prefix
        → if the total length of a is longger than b, a is placed after b.
        → SO, If Input list words is not following this, return ""

    Let me clarify this problem by using Some Exmaples:
    考えられるエッジケース
    ・同じ単語が含まれており、その単語間に別の単語がある場合それらはソートされていないことになる。
    →つまりDAGではなくサイクルが存在しているということになる。この際は空文字列を返却する必要がある。

    ・それぞれの順序が繋がっていない→その言語のソートされた単語情報だけでは順序を特定できず複数パターンある場合
    →複数の有効な順序がある場合は、どれか1つを返せばOKです。

    Post Order Traversal DFS
    子ノードを逆順から確定させていき、返却時に再度逆順にして答えとして返却する

    処理済みであるかを記録することで循環を防ぐ

    KEYWORD:
    ・DAG(Directed Acyclic Graph)→directed graph having not circle,
    ・Topological Sort
    ・Post Order DFS
    """
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word} # Chartcter: set

        for i in range(len(words) - 1): # comapare all two pairs.
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # having same prefix, but invalid ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: 
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # setting edge
                    break
        
        visit = {} # False = visited, True = visited & current path
        res = []

        def dfs(char: str):
            if char in visit: # key already exsist, it's meant already set the char
                return visit[char]

            visit[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True

            visit[char] = False
            res.append(char)
        
        for char in adj:
            if dfs(char):
                return ""
        
        return "".join(res[::-1])
        