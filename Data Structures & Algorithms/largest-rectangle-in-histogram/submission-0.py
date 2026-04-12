class Solution:
    """
    function should return the maximum value that means area of rectangle 

    area = minmum height * width(how many bars are there ?)
    or maxmum height * 1 
    
    example 1.
    Input: heights = [7,1,7,2,2,4]

    (i, j) = (0, 0) 7 * 1 = 1
    i

    first I want to think about Bruteforce solution.
    stack's top value is min height from 0 to i.

    monotically increasing stack

    高さが増加傾向にある場合は幅をそのまま拡張してよい
    ただし、自分より小さい高さである場合はその時点で幅の拡張は終了する

    """
    def largestRectangleArea_BurteForce(self, heights: List[int]) -> int:
        maxArea = 0
        
        for i in range(len(heights)):
            height = heights[i] # バーを固定したする

            rightMost = i + 1
            # 自分よりも右のバーが自分より小さい高さが現れるまで幅は拡張できる
            while rightMost < len(heights) and heights[rightMost] >= height: 
                rightMost += 1
            
            leftMost = i
            # 自分よりも(自分も含める)左より小さい高さが現れるまで幅は拡張できる
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            rightMost -= 1 # why ?
            leftMost += 1 # why ?
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
            print(maxArea)
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        stack内のバーは必ず増加傾向にあるはず
        対象となるバーの高さがstackのトップよりも
        高いならばそのままappendする
        低いならば、最新の要素の上から下まで対象のバーの高さ以下になるまでポップを繰り返す。
        ただし最終的に面積を求めたいので幅を計算するために(height, index)を一緒にstackに格納しておく必要がある。
        indexは自分よりも前のindexであり、その高さで取りうる幅

        """
        stack = [] # maybe monotonically increasing stack
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            # startを後方に拡張できるかわからないため、現在よりも高い過去のバーとも比較する
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

            print(stack)
                
        return maxArea
