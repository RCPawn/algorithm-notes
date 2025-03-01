"""
322. 零钱兑换
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
    计算并返回可以凑成总金额所需的 最少的硬币个数 。
    如果没有任何一种硬币组合能组成总金额，返回 -1 。
    你可以认为每种硬币的数量是无限的。
    示例 1：
            输入：coins = [1, 2, 5], amount = 11
            输出：3
            解释：11 = 5 + 5 + 1
    示例 2：
            输入：coins = [2], amount = 3
            输出：-1
    示例 3：
            输入：coins = [1], amount = 0
            输出：0
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # dp[i] 表示凑成金额 i 所需的最小硬币数
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # 对于金额 i，更新所需硬币数：
                # 取当前已有的 dp[i]（即凑成金额 i 已知的最少硬币数）和使用一枚 coin 后，
                # 加上凑成金额 (i - coin) 所需的硬币数（即 dp[i - coin] + 1）两者中的最小值。
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 2, 5]
print(coinChange(coins, 11))
