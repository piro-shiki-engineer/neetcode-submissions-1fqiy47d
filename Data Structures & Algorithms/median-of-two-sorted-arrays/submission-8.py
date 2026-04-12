class Solution:
    """

    nums1 = [1, 2, 3, 4, 4]
    nums2 = [3, 4, 5, 5]

    if jon num1 and num2

    nums_joined = [1,2,3,3,4,4,4,5,5]
    In this case, meadian is 4.


    Aim : We want to medina values which is tha array that it is joined nums1 and nums2.
    and what do you mean median ?

    let's think about each nums1 and nums2 median.
    first, let's see nums1
    nums1 = [1, 2, 3, 4, 4] nums1 median is just nums[2] whom index is 0 based because the length of nums1 is even.
    
    next, lets think about nums2
    nums2 = [3, 4, 5, 5] In this case, the length of nums2 is not even but odd.
    the value which is clalucated by like this (length(nums)the length of nums 

    BruteForce:
    Just join 2 arrays and retuning meadian.
    Time Complexity: O(n+m)

    Sol2:
    全体の中央値の左側は配列の長さから導出できる。
    長さのがより短い配列の値がもう一つの配列のどこに位置するかを二分探索を用いて特定することで、最終的な中央値が導出することができる。
    具体例を考えよう
    
    nums1 = [1, 2, 3, 4, 4]
    nums2 = [3, 4, 5, 5]

    In this case, the smaller length array is nums2

    [1,2,3,3,4,4,4,5,5] is result that which joined 2 arrays.
    left's partion is [1,2,3,3]
    right's partion is [4,4,5,5]

    if joined result is [1,2,3,3,4,4,4,5].
    left's partion is [1,2,3,3]
    right's partion is [4,4,5,5]
    meadian is (3+4) 2 = 3.5
    3 is right partion's most left
    4 is left partion's most right and you can get the this index just round down (the length devide 2)

    まず初めに短い配列のインデックス的に真ん中の値をを二分探索により求める。
    中央の値がもとまったことで小さい配列のうちさらに中央値以下の配列となる左側の配列が求められる
    
    つぎに大きい配列の中で小さい配列側の中央値以下となるような左側の部分となるようなインデックスをさらに二分探索する。
    この結果





    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 # 結合した際に中央より左配列の要素数

        if len(B) < len(A): # Aの配列が短い入れつという条件を実装を簡単にするために追加
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # ジョインいした時の中央値のインデックスを表す、

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j>= 0 else float("-infinity")
            Bright = B[j+1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd 
                if total % 2:
                    return min(Aright, Bright)
                # even
                return  (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        