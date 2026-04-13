class Solution:
    """
    Task: Return the lenght of the LCS betweeen text1 and text2

    * I define the text1 is longer or equals to text2.
    * There is no LCS, just return 0

    What is LCS ?
    it's ok no exactly contiunes

    Just Idea: Compute every charactres from each text1 and text2

    keyword:
    単語：和訳
    diagnoly: 斜めに
    Idiom:
    フレーズ：和訳

    Phase1. determine the next cell
    Check if 2 charcters matched or not, we move diagnoly cell.
        (i) If matched, need to solve subproblems, exclude mathced each characters.
        (ii) If not matched, we need to check next matched chars by moving right or down
    If the pointer is in out of bounds, Just return value 0


    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i + 1][j + 1] + 1
                else:
                    grid[i][j] = max(grid[i + 1][j], grid[i][j + 1])
        
        return grid[0][0]
        