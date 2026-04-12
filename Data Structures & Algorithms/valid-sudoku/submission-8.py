from collections import defaultdict

class Solution:
    """
    行、列、3x3マスすべてに重複なく1-9が配置することができる
    このboradとして有効であるかの判定
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set) # pointは3X3を1つとして扱うこと
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        
        return True

class Solution:
    """
    Task: Return True if the given grid is follow the definition of sudoku, return False if not so
    First Idea, Check wonder if that all cells following rules.
    Let me calarify this problem by using some samples.
    I think it's easy to check rule 1&2, but rule 3 is difficult.
    If we dont thik the rules, there are 9 digits that the empty cell can contain.
    Just check roms, culmns, 3*3 boxes can contain the each cells.

    why I cant solve this ?
    - How to manage the 3 * 3 cell can contain the cells. → 3で割った行番号と列番号をキーとして管理する
    
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in rows[i] or
                    board[i][j] in columns[j] or
                    board[i][j] in boxes[(i // 3, j // 3)]
                    ):
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[(i // 3, j // 3)].add(board[i][j])
        
        return True