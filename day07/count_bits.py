"""
338. 比特位计数
    给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，
    计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
    示例 1：
            输入：n = 2
            输出：[0, 1, 1]
            解释：
                0 --> 0
                1 --> 1
                2 --> 10
    示例 2：
            输入：n = 5
            输出：[0, 1, 1, 2, 1, 2]
            解释：
                0 --> 0, 1 --> 1
                2 --> 10, 3 --> 11
                4 --> 100, 5 --> 101
"""
from typing import List


# 方法一：
def countBits(n: int) -> List[int]:
    count_list = []
    for num in range(n + 1):
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num //= 2
        count_list.append(count)
    return count_list


# 方法二：
def countBits1(n):
    def count_ones(num):
        ones = 0
        while num > 0:
            # 消除二进制最低位的 1
            num &= (num - 1)
            # 每消除一个 1, ones + 1
            ones += 1
        return ones

    return [count_ones(num) for num in range(n + 1)]


print(countBits(5))
