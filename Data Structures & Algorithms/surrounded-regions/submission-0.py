class Solution:
    """
    Task: In-place the `O` cells which is four-derectionally surronded by "X" into "X"
    
    
    let me clarify the problem by describing some example.
    IDEA: DFS
    pesudo code
    1. determine cell from cells like the chacter is "O"
    2. inplce 
    3. check what if the four-directionally cells charcterer "O" or "X"
        3-1. if "X" or out of bounds, early return because we dont need search the next four-directionally cells 
        3-2. if "O" 

    Why I cant solve ?
    - 囲まれているとしてひっくり返していくというやり方をとったが最終的に囲まれていなかった時にひっくり返し直す方法がわからなかった

    """
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c): # DFS
            if (r < 0 or r == ROWS or c < 0 or c == COLS
                or board[r][c] != "O"):
                return
            board[r][c] = "T" # temporary
            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)
            
            
        # 1. (DFS) Capture unsrrounded regions
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)
        
        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"