"""
1323. 6 和 9 组成的最大数字
    给你一个仅由数字 6 和 9 组成的正整数 num。
    你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
    请返回你可以得到的最大数字。
    示例 1：
            输入：num = 9669
            输出：9969
            解释：
                改变第一位数字可以得到 6669 。
                改变第二位数字可以得到 9969 。
                改变第三位数字可以得到 9699 。
                改变第四位数字可以得到 9666 。
                其中最大的数字是 9969 。
    示例 2：
            输入：num = 9996
            输出：9999
            解释：将最后一位从 6 变到 9，其结果 9999 是最大的数。
    示例 3：
            输入：num = 9999
            输出：9999
            解释：无需改变就已经是最大的数字了。
"""


# 方法一：
def maximum69Number(num: int) -> int:
    s = str(num)
    first_six_index = -1
    n = len(s)
    for i in range(n):
        if s[i] == '6':
            first_six_index = i
            break
    res = ""
    for i in range(n):
        if i != first_six_index:
            res += s[i]
        else:
            res += '9'
    return int(res)


# 方法二：
def maximum69Number1(num):
    s = str(num)
    for c in s:
        if c == '6':
            '9'
            break
    return int(s)


# 方法三：
def maximum69Number2(num):
    return int(str(num).replace("6", "9", 1))


num = 9669
print(maximum69Number(num))
