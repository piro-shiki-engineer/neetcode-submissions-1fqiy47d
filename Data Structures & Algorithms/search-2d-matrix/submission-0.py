class Solution:
    """
    i th row first value is larger than i-1 th row last value.
    必ず昇順でソートされている。
    At first, we should determine the row that contains target.
    
    """
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     len(matrix[0])
    #     row, column = 0, 0

    #     while row < len(matrix):
            


    #         left = 0
    #         right
    #         while column < len(matrix[0]):
    #             if target < matrix[row][-1]:
    #             column += 1

    #         row += 1

    #         target_row_index += 1

    #     return false


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix):
            column = 0

            while column < len(matrix[0]):
                if matrix[row][column] == target:
                    return True
                column += 1
            row += 1
        
        return False