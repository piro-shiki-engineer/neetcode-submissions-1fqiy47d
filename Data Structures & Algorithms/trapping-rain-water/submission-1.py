class Solution:
    def trap(self, height: List[int]) -> int:
        """
        バーの間に水の総体積を求めよ
        height = [0,2,0,3,1,0,1,3,2,1]

        あるバー位相点に着目したときに
        着目するバーの高さ＝（そのバーの高さ）ー（そのバーを挟む棒の最小値）がそのバー上に体積できる水
        
        バーの最初と最後はチェックする必要がない

        height = [0,2,0,4,1,3,2,1,3,2,1]

        i=0 area = 0
        i=1 area = abs(height[1]) * max(hei)
        i=2 area = height[1] - height[2] = 2 - 0 = 2
        """

        if len(height) == 0:
            return 0

        n = len(height)
        ans = 0
        forward_max_height = [0] * n
        backward_max_height = [0] * n

        forward_max_height[0] = height[0]
        backward_max_height[-1] = height[-1]

        for i in range(1, n):
            forward_max_height[i] = max(forward_max_height[i-1], height[i])
        
        for i in range(n-2, -1, -1):
            backward_max_height[i] = max(backward_max_height[i+1], height[i])

        for i in range(n):
            ans += min(forward_max_height[i], backward_max_height[i]) - height[i]

        return ans

    def trap2(self, height: List[int]) -> int:
        """
        単調スタック(Monotonic Stack)を利用した解答

        単調スタック
        - スタックを常に単調増加(または単調減少)に保つ
        - 追加する場合は末端の値に比べて小さい（大きい）場合は、満たさない値を満たすまでポップしてから追加
        - そうでない場合は、そのまま追加する
        """
        return 0

    def best_trap(self, height: List[int]) -> int:
        """
        O(1)
        Two Pointerを使った解答
        その時点でのleftMaxとrightMaxの二つのポインターで保持する
        二つのポインターを比較したときに小さい方のポインターを動かす
        二つの値が同じ時は、左（または右）がシフトするよう決める
        そのバーで蓄えている水はそのバーの（右左それぞれから見た時の最大値の小さい方）-（そのバーの高さ）
        この値が負になるならば、0を加算すればいい
        """
        if not height:
            return 0
        
        res = 0
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]

            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return ans