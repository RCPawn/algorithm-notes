"""
2656. K 个元素的最大和
    给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
    你需要执行以下操作 恰好 k 次，最大化你的得分：
    1. 从 nums 中选择一个元素 m 。
    2. 将选中的元素 m 从数组中删除。
    3. 将新元素 m + 1 添加到数组中。
    4. 你的得分增加 m 。
    请你返回执行以上操作恰好 k 次后的最大得分。
    示例 1：
            输入：nums = [1,2,3,4,5], k = 3
            输出：18
            解释：我们需要从 nums 中恰好选择 3 个元素并最大化得分。
            第一次选择 5 。和为 5 ，nums = [1,2,3,4,6] 。
            第二次选择 6 。和为 6 ，nums = [1,2,3,4,7] 。
            第三次选择 7 。和为 5 + 6 + 7 = 18 ，nums = [1,2,3,4,8] 。
            所以我们返回 18 。
            18 是可以得到的最大答案。
    示例 2：
            输入：nums = [5,5,5], k = 2
            输出：11
            解释：我们需要从 nums 中恰好选择 2 个元素并最大化得分。
            第一次选择 5 。和为 5 ，nums = [5,5,6] 。
            第二次选择 6 。和为 6 ，nums = [5,5,7] 。
            所以我们返回 11 。
            11 是可以得到的最大答案。
"""
from typing import List


# 方法一：
def maximizeSum(nums: List[int], k: int) -> int:
    max_score = 0
    while k > 0:
        selected = max(nums)
        nums.remove(selected)
        nums.append(selected + 1)
        max_score += selected
        k -= 1
    return max_score


# 方法二：
def maximizeSum1(nums, k):
    return (2 * max(nums) + k - 1) * k // 2


print(maximizeSum([1, 2, 3, 4, 5], 3))
