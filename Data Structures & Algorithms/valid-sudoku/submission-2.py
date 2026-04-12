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
        