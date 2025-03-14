"""
62. 不同路径
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
    机器人每次只能向下或者向右移动一步。
    机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
    问总共有多少条不同的路径？
    示例 1：
            输入：m = 3, n = 7
            输出：28
    示例 2：
            输入：m = 3, n = 2
            输出：3
            解释：从左上角开始，总共有 3 条路径可以到达右下角。
                    1. 向右 -> 向下 -> 向下
                    2. 向下 -> 向下 -> 向右
                    3. 向下 -> 向右 -> 向下
    示例 3：
            输入：m = 7, n = 3
            输出：28
    示例 4：
            输入：m = 3, n = 3
            输出：6
"""

from math import comb


# 方法一：
def unique_paths(m, n):
    return comb(m + n - 2, m - 1)


# 方法二：
def unique_paths1(m, n):
    # 这里计算组合数 C(m+n-2, n-1)
    # 为减少乘除次数，可将较小的 (n-1) 放到循环里
    if n > m:
        # 保证 n-1 是较小的那个
        m, n = n, m

    total_steps = m + n - 2  # 总步数
    down_steps = n - 1  # 或者右移 steps = m - 1, 看你选哪个

    result = 1
    for i in range(1, down_steps + 1):
        # 依次相乘/相除，避免大阶乘
        result = result * (total_steps - i + 1) // i
    return result


# 方法三：
def unique_paths2(m: int, n: int) -> int:
    # 初始化一个长度为 n 的列表 f，每个元素初始值为 1。
    # 这里 f[j] 表示当前行中到达第 j 列的路径数，
    # 第一行所有位置只能从左侧一步步走过来，所以路径数都为 1。
    f = [1] * n

    # 从第二行开始遍历（因为第一行已经初始化好了）
    for i in range(1, m):
        # 从第二列开始遍历（第 0 列在任何情况下都是 1，因为只能从上方过来）
        for j in range(1, n):
            # 更新 f[j]：
            # f[j] 原来的值表示从上一行到达当前位置（即“上方”）的路径数，
            # f[j - 1] 表示在当前行中，左侧单元格的路径数（即“左侧”）。
            # 两者相加就是当前单元格的路径数，因为机器人只能向右或向下移动。
            f[j] += f[j - 1]

    # f[n - 1] 最终保存的是最后一列的值，也就是最后一行、右下角单元格的路径数
    return f[n - 1]



print(unique_paths(3, 7))
