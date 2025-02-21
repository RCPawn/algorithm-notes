"""
LCR 161. 连续天数的最高销售额
    某公司每日销售额记于整数数组 sales，
    请返回所有 连续 一或多天销售额总和的最大值。
    要求实现时间复杂度为 O(n) 的算法。
    示例 1：
            输入：sales = [-2,1,-3,4,-1,2,1,-5,4]
            输出：6
            解释：[4,-1,2,1] 此连续四天的销售总额最高，为 6。
    示例 2：
            输入：sales = [5,4,-1,7,8]
            输出：23
            解释：[5,4,-1,7,8] 此连续五天的销售总额最高，为 23。
"""
from typing import List


def maxSales(sales: List[int]) -> int:
    max_sum = current_sum = sales[0]

    for sale in sales[1:]:
        # 如果当前子数组的和加上新的元素 sale 小于当前元素 sale，
        # 说明从当前元素重新开始计算子数组更好。
        current_sum = max(sale, current_sum + sale)
        max_sum = max(max_sum, current_sum)

    return max_sum


sales = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSales(sales))
