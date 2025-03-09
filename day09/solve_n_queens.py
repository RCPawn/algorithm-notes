"""
51. N 皇后
    按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
    n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
    每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    示例 1：
            输入：n = 4
            输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
            解释：如上图所示，4 皇后问题存在两个不同的解法。
    示例 2：
            输入：n = 1
            输出：[["Q"]]
"""
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    res = []
    # 初始化棋盘，'.' 表示空位
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(row, col) -> bool:
        # 检查当前列是否有冲突
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # 检查左上对角线是否有冲突
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 检查右上对角线是否有冲突
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            res.append([''.join(r) for r in board])
            return

        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return res


print(solveNQueens(4))
