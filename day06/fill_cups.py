"""
2335. 装满杯子需要的最短总时长
    现有一台饮水机，可以制备冷水、温水和热水。
    每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。
    给你一个下标从 0 开始、长度为 3 的整数数组 amount ，
    其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。
    返回装满所有杯子所需的 最少 秒数。
    示例 1：
            输入：amount = [1,4,2]
            输出：4
            解释：下面给出一种方案：
            第 1 秒：装满一杯冷水和一杯温水。
            第 2 秒：装满一杯温水和一杯热水。
            第 3 秒：装满一杯温水和一杯热水。
            第 4 秒：装满一杯温水。
            可以证明最少需要 4 秒才能装满所有杯子。
    示例 2：
            输入：amount = [5,4,4]
            输出：7
            解释：下面给出一种方案：
            第 1 秒：装满一杯冷水和一杯热水。
            第 2 秒：装满一杯冷水和一杯温水。
            第 3 秒：装满一杯冷水和一杯温水。
            第 4 秒：装满一杯温水和一杯热水。
            第 5 秒：装满一杯冷水和一杯热水。
            第 6 秒：装满一杯冷水和一杯温水。
            第 7 秒：装满一杯热水。
    示例 3：
            输入：amount = [5,0,0]
            输出：5
            解释：每秒装满一杯冷水。
"""

from typing import List


# 方法一：
def fillCups(amount: List[int]) -> int:
    seconds = 0
    while sum(amount) > 0:
        amount.sort()
        if amount[2] > 0:
            amount[2] -= 1
        if amount[1] > 0:
            amount[1] -= 1
        seconds += 1
    return seconds


# 方法二：
def fillCups1(amount: List[int]) -> int:
    return max(max(amount), (sum(amount) + 1) // 2)


# 方法三：
def fillCup2(amount):
    amount.sort()
    return (amount[2] if amount[2] > amount[1] + amount[0]
            else (sum(amount) + 1) // 2)


# 4, 4, 5
# 4, 3, 4
# 3, 3, 3
# 2, 2, 3
# 1, 2, 2
# 1, 1, 1
# 0, 0, 1
# 0, 0, 0
print(fillCups([5, 4, 4]))  # 输出: 7
print(fillCups([1, 4, 2]))  # 输出: 4
print(fillCups([5, 0, 0]))  # 输出: 5
