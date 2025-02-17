"""
1137. 第 N 个泰波那契数
    泰波那契序列 Tn 定义如下：
    T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
    给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
    示例 1：
            输入：n = 4
            输出：4
            解释：
                T_3 = 0 + 1 + 1 = 2
                T_4 = 1 + 1 + 2 = 4
    示例 2：
            输入：n = 25
            输出：1389537
"""


# 方法一：
def tribonacci(n: int) -> int:
    t = [0, 1, 1]
    if n < 3:
        return t[n]
    for i in range(3, n + 1):
        t.append(t[i - 1] + t[i - 2] + t[i - 3])
    return t[n]


# 方法二：
def tribonacci1(n):
    if n < 3:
        return [0, 1, 1][n]
    t = [0, 1, 1] + [0] * (n - 2)
    for i in range(3, n + 1):
        t[i] = t[i - 1] + t[i - 2] + t[i - 3]
    return t[n]


print(tribonacci(4))
