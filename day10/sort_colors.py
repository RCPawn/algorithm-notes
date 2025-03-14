"""
75. 颜色分类
    给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
    原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    必须在不使用库内置的 sort 函数的情况下解决这个问题。
    示例 1：
            输入：nums = [2,0,2,1,1,0]
            输出：[0,0,1,1,2,2]
    示例 2：
            输入：nums = [2,0,1]
            输出：[0,1,2]
"""
from itertools import count
from typing import List


# 方法一：
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    """n = len(nums)
    count_0 = nums.count(0)
    count_1 = nums.count(1)

    for i in range(n):
        if i < count_0:
            nums[i] = 0
        elif i < count_0 + count_1:
            nums[i] = 1
        elif i < n:
            nums[i] = 2"""

    nums[:] = [0] * nums.count(0) + [1] * nums.count(1) + [2] * nums.count(2)


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
