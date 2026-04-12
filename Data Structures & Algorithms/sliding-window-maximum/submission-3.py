from collections import deque

class Solution:
    """
    numsにおける各位置でのwindow内における最大値を求める問題

    windowをずらした時の

    Brute Force
    time complexity O(N*k) n means the lenght of the input array nums.
    space comoplxity O(N)

    More efficiently tiem O(N) by using deque

    Input: nums = [1,2,1,0,4,2,6], k = 3
    Output: [2,2,4,4,6]


    Monotinicily Decreasing Queue(単調減少キュー)

    通常の priority queue は:
    要素の追加と最小(または最大)要素の取り出しができる
    要素は任意の順序で追加できる
    優先度は任意の値を取ることができる

    一方、monotone priority queue は:

    単調性(monotonicity)という制約が追加される
    追加される要素の優先度が単調増加または単調減少である必要がある
    つまり、新しく追加される要素の優先度は、直前に追加された要素の優先度より必ず大きい(または小さい)必要がある


    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = right = 0 # use two pointer for window
        queue = deque() # index

        while right < len(nums):
            # pop index of smaller value from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            # remove index of left value from window
            if left > queue[0]:
                queue.popleft()
            
            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1
            
            right += 1

        return output
        