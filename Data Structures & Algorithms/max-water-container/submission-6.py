import heapq


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        2本の蓄積することができる水が必要になる
        2本の棒高さの最低値*二つの棒の位相差

        heights = [1,7,2,5,4,7,3,6]
        width は線形に増える
        min(1, 7) * abs(1-0) = 1
        min(1, 2) * abs(2-0) = 2
        min(1, 5) * abs(3-0) = 5
        min(1, 4) * abs(4-0) = 4
        min(1, 7) * abs(5-0) = 7
        min(1, 3) * abs(6-0) = 3
        min(1, 6) * abs(7-0) = 7

        Bottleneck is lower height.
        体積の最大化が目的
        二つのインデックスとその体積をheapにいれる→O(n^2)になってしまう
        """
        # BRUTE FORCE
        # ans = 0
        # n = len(heights)
        # for i in range(n):
        #     j = n-1
        #     while i < j:
        #         volume = min(heights[i], heights[j]) * abs(j-i)
        #         ans = max(ans, volume)
        #         j -= 1
        # return ans

        #BEST
                # BEST
        ans = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            ans = max(ans, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans


        