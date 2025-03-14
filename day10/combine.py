"""
77. 组合
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    你可以按 任何顺序 返回答案。
    示例 1：
            输入：n = 4, k = 2
            输出：
            [
              [2,4],
              [3,4],
              [2,3],
              [1,2],
              [1,3],
              [1,4],
            ]
    示例 2：
            输入：n = 1, k = 1
            输出：[[1]]
"""
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(1, [])
    return result


print(combine(4, 2))
