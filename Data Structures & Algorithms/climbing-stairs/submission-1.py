class Solution:
    """
    dfs的に行ってもいいが途中経過のtotalが同じ値をとることを利用すればより効率てきなに処理できる

    memoizationメモ化
    動的に現在のtotal値によって更なる部分問題が生成されるためdp問題となる

    dfs(backtrack)topdown→メモ化できるならdpにとらえなおすbotomup

    dpテーブルは0-5のindexをでありbase_case はnである。
    つまりbase caseから分岐を発生させていく
    5からbase case
    base caseに辿り着くには4から1上がる場合のみである。

    既に条件を満たしている状態」を適切に初期化
    iの場合の数を満たすにはそこから見た時のoneステップ目つまりはdp[i+1], twoステップ目のdp[i+2]で求められる
    n-1回この比較を繰り返す
    """
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

            # one, two = one + two, one
        
        return one

    def climbStairs_dfs_brute(self, n: int) -> int:
        res = 0

        def dfs(total):
            nonlocal res
            if total == n:
                res += 1
                return

            elif total > n:
                return
            
            for steps in [1, 2]:
                dfs(total + steps)

        for steps in [1, 2]:
            dfs(steps)
        
        return res
