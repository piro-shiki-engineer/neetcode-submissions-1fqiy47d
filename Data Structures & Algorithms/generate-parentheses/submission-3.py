class Solution:
    """
     Parentheses　ぺれんてしー　括弧
    カッコの組み合わせを作る過程を考えてみる
    n = 1 ()
    n = 2 (), ()(), (())
    n = 3 (), ()(), (()), ()(), (()), ()()(), (()()), (())(), ((()))
        重複を除くと、(), ()(), (()), ()()(), (()()), (())(), ((()))
        n = 1 の結果のうち一つ一つに下記操作を行う
        (ⅰ) （）を横に並べる
        (ⅱ) ()で囲む
        
    """
    def myfirst_generateParenthesis(self, n: int) -> List[str]:
        """
        n = n - 1 の結果のうち一つ一つに下記操作を行う
            (ⅰ) （）を横に右、左に並べる
            (ⅱ) ()で囲む

        出力がまずおかしい → 最も近い回答：バックトラッキング（ブルートフォース）
        
        """
        res = ["()"]
        
        i = 1
        while i < n:
            j = 0
            res_i = []
            for res_j in res:
                res_i.append("()" + res_j)
                res_i.append(res_j + "()")
                res_i.append("(" + res_j + ")")

            res = list(set(res_i)) 
            i += 1
            

        return list(set(res))

    def generateParenthesis(self, n: int) -> List[str]:
        """
        バックトラッキング：        
        The following is a general outline of how a backtracking algorithm works:
        1. Choose an initial solution.
        2. Explore all possible extensions of the current solution.
        3. If an extension leads to a solution, return that solution.
        4. If an extension does not lead to a solution, backtrack to the previous solution and try a different extension.
        5. Repeat steps 2-4 until all possible solutions have been explored.

        Definitely, start OPEN parenthese

        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # これにより一つ前の状態に戻っていることになる

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

