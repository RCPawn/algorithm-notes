"""
152. 乘积最大子数组
    给你一个整数数组 nums ，请你找出数组中乘积最大的
    非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
    测试用例的答案是一个 32-位 整数。
    示例 1:
            输入: nums = [2,3,-2,4]
            输出: 6
            解释: 子数组 [2,3] 有最大乘积 6。
    示例 2:
            输入: nums = [-2,0,-1]
            输出: 0
            解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


def maxProduct(nums: List[int]) -> int:
    cur_max = cur_min = res = nums[0]

    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max

        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)

        res = max(res, cur_max)

    return res


nums = [2, 3, -2, 4]
print(maxProduct(nums))
