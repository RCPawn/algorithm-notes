"""
17. 电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    案可以按 任意顺序 返回。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    示例 1：
            输入：digits = "23"
            输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    示例 2：
            输入：digits = ""
            输出：[]
    示例 3：
            输入：digits = "2"
            输出：["a","b","c"]
"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    letter_dict = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    res = []

    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return

        for c in letter_dict[digits[index]]:
            backtrack(index + 1, path + c)

    backtrack(0, "")
    return res


digits = "23"
print(letterCombinations(digits))
