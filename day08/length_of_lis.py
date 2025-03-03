"""
300. 最长递增子序列
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
    子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
    例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
    示例 1：
            输入：nums = [10,9,2,5,3,7,101,18]
            输出：4
            解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
    示例 2：
            输入：nums = [0,1,0,3,2,3]
            输出：4
    示例 3：
            输入：nums = [7,7,7,7,7,7,7]
            输出：1
"""
import bisect
from typing import List


# 方法一：动态规划 (O(n²))
def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# 方法二：贪心 + 二分查找 (O(n log n))
def lengthOfLIS1(nums: List[int]) -> int:
    tails = []
    for num in nums:
        # 在 tails 中查找第一个不小于 num 的位置
        index = bisect.bisect_left(tails, num)
        # 如果 num 大于 tails 中所有元素，则添加到末尾
        if index == len(tails):
            tails.append(num)
        # 替换，确保每个长度对应的尾值尽可能小
        else:
            tails[index] = num
    return len(tails)


# 方法三：暴力回溯（超时）
def lengthOfLIS2(nums: List[int]) -> int:
    n = len(nums)
    best = 0

    def backtrack(index: int, prev: int, length: int):
        nonlocal best
        if index == n:
            best = max(best, length)
            return
        # 不选择当前数字，直接进入下一个
        backtrack(index + 1, prev, length)
        # 选择当前数字（如果符合递增要求）
        if prev is None or nums[index] > prev:
            backtrack(index + 1, nums[index], length + 1)

    backtrack(0, None, 0)
    return best


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
