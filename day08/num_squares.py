"""
279. 完全平方数
    给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
    完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
    例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
    示例 1：
            输入：n = 12
            输出：3
            解释：12 = 4 + 4 + 4
    示例 2：
            输入：n = 13
            输出：2
            解释：13 = 4 + 9
"""


# 0 -> 0
# 1 -> 0
# 2 -> 0
# 3 -> 0
# 4 -> 1
def numSquares(n: int) -> int:
    dp = [n + 1] * (n + 1)
    dp[0] = 0

    # 生成所有不超过 n 的完全平方数
    squares = [i * i for i in range(1, int(n**0.5) + 1)]

    for i in range(1, n + 1):
        for square in squares:
            if i < square:
                break  # 剪枝，后面的平方数更大，不可能构成 i
            dp[i] = min(dp[i], dp[i - square] + 1)

    return dp[n]


# 测试
print(numSquares(12))  # 输出: 3 (12 = 4 + 4 + 4)
print(numSquares(13))  # 输出: 2 (13 = 4 + 9)

