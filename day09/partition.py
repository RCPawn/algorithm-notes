"""
131. 分割回文串
    给你一个字符串 s，请你将 s 分割成一些 子串，
    使每个子串都是 回文串 。返回 s 所有可能的分割方案。
    示例 1：
            输入：s = "aab"
            输出：[["a","a","b"],["aa","b"]]
    示例 2：
            输入：s = "a"
            输出：[["a"]]
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    def backtrack(start, path):
        n = len(s)
        if start == n:
            res.append(path.copy())
            return

        for end in range(start, n):
            sub_str = s[start:end + 1]
            if sub_str == sub_str[::-1]:
                path.append(sub_str)
                backtrack(end + 1, path)
                path.pop()

    res = []
    backtrack(0, [])
    return res


s = "aab"
print(partition(s))
