"""
416. 分割等和子集
    给你一个 只包含正整数 的 非空 数组 nums 。
    请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    示例 1：
            输入：nums = [1,5,11,5]
            输出：true
            解释：数组可以分割成 [1, 5, 5] 和 [11] 。
    示例 2：
            输入：nums = [1,2,3,5]
            输出：false
            解释：数组不能分割成两个元素和相等的子集。
"""
from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    # dp[cur_sum] 表示是否可以凑出和 cur_sum
    # 和为 0 总是可以的
    dp = [True] + [False] * target

    for num in nums:
        # 从 target 开始倒序更新，防止重复使用同一个数字
        for cur_sum in range(target, num - 1, -1):
            # 如果可以组成和为 cur_sum - num 的子集，
            # 那么加上当前数字 num 后，就可以组成和为 cur_sum 的子集。
            dp[cur_sum] = dp[cur_sum] or dp[cur_sum - num]

    return dp[target]


nums = [1, 5, 11, 5]
print(canPartition(nums))
