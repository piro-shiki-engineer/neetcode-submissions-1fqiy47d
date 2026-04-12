class Solution:
    """
    i th row first value is larger than i-1 th row last value.
    必ず昇順でソートされている。
    At first, we should determine the row that contains target.
    
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
    Output: true



    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        
        top, bot = 0, rows - 1
        while top <= bot: # 列方向の二分探索 行を特定する目的
            center_row = (top + bot) // 2
            if target > matrix[center_row][-1]: # targetが行末の値より大きい
                top = center_row + 1
            
            elif target < matrix[center_row][0]: # targetが行頭の値より大きい
                bot = center_row - 1

            else: #二つの条件を満たさないときにその行にtargetが存在する
                break

        if not(top <= bot): #
            return False
        
        center_row = (top + bot) // 2
        left, right = 0, columns - 1 
        while left <= right:
            center = (left + right) // 2
            if target > matrix[center_row][center]:
                left = center + 1
            elif target < matrix[center_row][center]:
                right = center - 1
            else:
                return True
        
        return False

    def searchMatrix_BruteForce(self, matrix: List[List[int]], target: int) -> bool:
        """
        単純に全て参照してtargeが見つかればTrue,　最後まで見てなければFalse
        Time Complexity: O(n*m)
        """
        row = 0
        while row < len(matrix):
            column = 0

            while column < len(matrix[0]):
                if matrix[row][column] == target:
                    return True
                column += 1
            row += 1
        
        return False