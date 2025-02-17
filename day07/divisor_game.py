"""
1025. 除数博弈
    爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
    最初，黑板上有一个数字 n 。在每个玩家的回合，玩家需要执行以下操作：
    选出任一 x，满足 0 < x < n 且 n % x == 0 。
    用 n - x 替换黑板上的数字 n 。
    如果玩家无法执行这些操作，就会输掉游戏。
    只有在爱丽丝在游戏中取得胜利时才返回 true 。
    假设两个玩家都以最佳状态参与游戏。
    示例 1：
            输入：n = 2
            输出：true
            解释：爱丽丝选择 1，鲍勃无法进行操作。
    示例 2：
            输入：n = 3
            输出：false
            解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""


# 方法一：
def divisorGame(n: int) -> bool:
    return n % 2 == 0


# 方法二：
def divisor_game(n):
    dp = [False] * (n + 1)
    dp[1] = False
    for i in range(2, n + 1):
        for x in range(1, i):
            # Alice 能选出合法数
            # 并且能让 Bob 在面临下一个数 i - x 时无法选出合法数
            if i % x == 0 and not dp[i - x]:
                dp[i] = True
                break
    return dp[n]


print(divisor_game(3))
