class Solution:
    """
    diagonaly: 斜めに

    Task: how to place N queens in N * N grid. queens directions dont cover each directions.
    I want use the breteforce as known also backtracking.

    To using the backtracking, we need the rule when need to back track.
    A queen in a chessboard can attack horizontally, vertically, and diagonally.
    - if we want to place one queen, we need check the state like already cover by the other queens.

    自分の間違っていた方針
    一つのクイーン配置位置をグリッド全てを対象としてしまっている。
    → 各行の一つのクイーンしか配置できない、各列にも一つしかおけないという制約を行と列のどちらかをsetで管理する

    また傾き正の斜線と傾き負の斜線を利用済みかどうかもsetで管理する。
    どの傾き負の斜線を利用したかは行のindexを示す値rと列のindxを示すlの差r-cで分類できる
    どの傾き正の斜線を利用したかは行のindexを示す値rと列のindxを示すlの差r+cで分類できる
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        board = [["." for j in range(n)] for i in range(n)]
        res = []

        def backtracking(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtracking(r + 1)

                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backtracking(0)
        return res
