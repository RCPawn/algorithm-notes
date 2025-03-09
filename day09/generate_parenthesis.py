"""
    数字 n 代表生成括号的对数，请你设计一个函数，
    用于能够生成所有可能的并且 有效的 括号组合。
    示例 1：
            输入：n = 3
            输出：["((()))","(()())","(())()","()(())","()()()"]
    示例 2：
            输入：n = 1
            输出：["()"]
"""
from typing import List


# 方法一：
def generateParenthesis(n: int) -> List[str]:
    res = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            # 递归返回时，自动回到上一层继续执行未完成的部分。
            return
        # 只要左括号数量没到n，就可以添加 '('
        if left < n:
            backtrack(s + '(', left + 1, right)
        # 右括号数量必须小于左括号数量才能添加 ')'
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack("", 0, 0)
    return res


# 方法二：
def generateParenthesis1(n: int) -> List[str]:
    ans = []

    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append('(')
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return ans


print(generateParenthesis(2))
