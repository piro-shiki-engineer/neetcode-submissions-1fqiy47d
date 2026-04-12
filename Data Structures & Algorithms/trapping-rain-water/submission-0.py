from collections import defaultdict

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

