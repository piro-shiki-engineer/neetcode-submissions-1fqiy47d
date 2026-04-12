class Solution:
    """
    i th row first value is larger than i-1 th row last value.
    必ず昇順でソートされている。
    At first, we should determine the row that contains target.
    
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
    Output: true



    """
    def searchMatrix_BEST(self, matrix: List[List[int]], target: int) -> bool:
        """
        targetが存在する行をまず特定する
        次にtargetが存在する行のどこの列に存在するかも求めている
        Time Complexity: O(logm + logn) = O(log(m*n))
        """
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

        if not(top <= bot): # targetのある行がない場合用の早期リターン
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

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        targetが存在する行をまず特定する
        次にtargetが存在する行のどこの列に存在するかも求めている
        Time Complexity: O(log(m*n))
        """
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1 
        while left <= right:
            center = left + (right - left) // 2
            row, col = center // columns, center % columns
            if target > matrix[row][col]:
                left = center + 1
            elif target < matrix[row][col]:
                right = center - 1
            else:
                return True
        
        return False    
    
    def searchMatrix_BruteForce(self, matrix: List[List[int]], target: int) -> bool:
        """
        単純に全て参照してtargeが見つかればTrue, 最後まで見てなければFalse
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