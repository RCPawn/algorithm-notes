"""
79. 单词搜索
    给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
    如果 word 存在于网格中，返回 true ；否则，返回 false 。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，
    其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
    同一个单元格内的字母不允许被重复使用。
    示例 1：
            输入：board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ], word = "ABCCED"
            输出：true
    示例 2：
            输入：board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ], word = "SEE"
            输出：true
    示例 3：
            输入：board = [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ], word = "ABCB"
            输出：false
"""
from typing import List


# 方法一：
def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    rows, cols = len(board), len(board[0])

    def dfs(i, j, index):
        # 当遍历完 word 中所有字符时，说明找到了单词
        if index == len(word):
            return True
                                                                                                                                 
        # 检查索引合法性及当前字符是否匹配
        if (i < 0 or i >= rows
                or j < 0 or j >= cols
                or board[i][j] != word[index]):
            return False

        # 避免重复使用
        temp = board[i][j]
        board[i][j] = '#'

        # 递归搜索四个方向：上、下、左、右
        found = (dfs(i + 1, j, index + 1) or
                 dfs(i - 1, j, index + 1) or
                 dfs(i, j + 1, index + 1) or
                 dfs(i, j - 1, index + 1))

        board[i][j] = temp  # 恢复现场
        return found

    # 仅从与 word 第一个字符匹配的点开始搜索
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True

    return False


# 方法二：
def exist1(board: List[List[str]], word: str) -> bool:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check(i: int, j: int, k: int) -> bool:
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.add((i, j))
        result = False
        for di, dj in directions:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if (newi, newj) not in visited:
                    if check(newi, newj, k + 1):
                        result = True
                        break

        visited.remove((i, j))
        return result

    h, w = len(board), len(board[0])
    visited = set()
    for i in range(h):
        for j in range(w):
            if check(i, j, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCCED"

print(exist(board, word))
