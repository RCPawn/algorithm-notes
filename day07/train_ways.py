"""
LCR 127. 跳跃训练
    今天的有氧运动训练内容是在一个长条形的平台上跳跃。
    平台有 num 个小格子，每次可以选择跳 一个格子 或者 两个格子。
    请返回在训练过程中，学员们共有多少种不同的跳跃方式。
    结果可能过大，因此结果需要取模 1e9+7（1000000007），
    如计算初始结果为：1000000008，请返回 1。
    示例 1：
            输入：n = 2
            输出：2
    示例 2：
            输入：n = 5
            输出：8
"""

"""
    f(n) = f(n - 1) + f(n - 2)
"""


# 方法一：
def trainWays(num: int) -> int:
    a, b = 1, 1
    for _ in range(num):
        a, b = b, (a + b) % 1000000007
    return a


# 方法二：
def train_ways(num):
    ways = [1] * (num + 1)
    for i in range(2, num + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % 1000000007
    return ways[num]


print(trainWays(5))
