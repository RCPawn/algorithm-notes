"""
3174. 清除数字
    给你一个字符串 s 。
    你的任务是重复以下操作删除 所有 数字字符：
    删除 第一个数字字符 以及它左边 最近 的 非数字 字符。
    请你返回删除所有数字字符以后剩下的字符串。
    示例 1：
            输入：s = "abc"
            输出："abc"
            解释：字符串中没有数字。

    示例 2：
            输入：s = "cb34"
            输出：""
            解释：一开始，我们对 s[2] 执行操作，s 变为 "c4" 。
                 然后对 s[1] 执行操作，s 变为 "" 。
"""


def clearDigits(s: str) -> str:
    stack = []
    for c in s:
        if c.isdigit():
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


s = "cb34"
print(clearDigits(s))
