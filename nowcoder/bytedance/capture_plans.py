"""
    给定 N 个建筑物（坐标已从小到大排序）以及一个整数 D。
    现需要从中选取 3 个不同建筑物作为埋伏点，
    要求这 3 个点中距离最远的两个建筑物之间的距离不超过 D。
    求满足条件的三元组数量，结果对 99997867 取模。
    输入：

    第一行：两个整数 N 和 D，分别表示建筑物数和允许的最大距离（1 ≤ N, D ≤ 10^6）。
    第二行：N 个建筑物的位置（整数，范围 [0, 10^6]），已按升序排列。
    输出：
    一个数字，表示满足条件的不同方案数，对 99997867 取模。
    示例1：
        输入：
            4 3
            1 2 3 4
        输出：
            4
            说明：可选方案 (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)
    示例2：
        输入：
            5 19
            1 10 20 30 50
        输出：
            1
        说明：可选方案 (1, 10, 20)
    示例3
        输入：
            2 100
            1 102
        输出：
            0
        说明：无可选方案
"""
import sys


def main():
    data = sys.stdin.read().split()
    N, D = int(data[0]), int(data[1])
    positions = list(map(int, data[2:2 + N]))
    res = j = 0

    for i in range(N):
        # 找到第一个不满足 positions[j] - positions[i] <= D 的位置
        while j < N and positions[j] - positions[i] <= D:
            j += 1

        # 在区间 [i+1, j-1] 内的建筑物数目
        count = j - i - 1

        # 如果 count 至少为 2，说明可以在这个区间内选取两个点，与 positions[i] 形成一个三元组
        if count >= 2:
            # 组合数 C(count, 2) 计算从 count 个建筑物中选取任意两个的方法数
            res = (res + count * (count - 1) // 2) % 99997867
    sys.stdout.write(str(res))


if __name__ == '__main__':
    main()
