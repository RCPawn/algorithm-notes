"""
    LCR 187. 破冰游戏
        社团共有 num 位成员参与破冰游戏，编号为 0 ~ num-1。
        成员们按照编号顺序围绕圆桌而坐。
        社长抽取一个数字 target，从 0 号成员起开始计数，
        排在第 target 位的成员离开圆桌，且成员离开后从下一个成员开始计数。
        请返回游戏结束时最后一位成员的编号。
        示例 1：
                输入：num = 7, target = 4
                输出：1
        示例 2：
                输入：num = 12, target = 5
                输出：0
"""


# 方法一：
def iceBreakingGame(num: int, target: int) -> int:
    if num == 1:
        return 0
    return (iceBreakingGame(num - 1, target) + target) % num


# 方法二：
def iceBreakingGame1(num: int, target: int) -> int:
    res = 0  # 当 num = 1 时，结果是 0
    for i in range(2, num + 1):  # 从 2 开始，逐步计算
        res = (res + target) % i
    return res


print(iceBreakingGame(12, 5))
