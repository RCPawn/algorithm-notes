"""
78. 子集
    给你一个整数数组 nums ，数组中的元素 互不相同 。
    返回该数组所有可能的子集（幂集）。
    解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
    示例 1：
            输入：nums = [1,2,3]
            输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    示例 2：
            输入：nums = [0]
            输出：[[],[0]]
"""
from typing import List


# 方法一：
def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start: int, path: List[int]):
        res.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res


# 方法二：
def subsets1(nums):
    res = []
    n = len(nums)
    # visited[i] 表示第 i 个元素是否被选中
    visited = [False] * n

    def dfs(i: int):
        # 当遍历完所有元素时，根据 visited 数组构造当前子集
        if i == n:
            subset = [nums[j] for j in range(n) if visited[j]]
            res.append(subset)
            return
        # 不选第 i 个元素
        visited[i] = False
        dfs(i + 1)
        # 选第 i 个元素
        visited[i] = True
        dfs(i + 1)

    dfs(0)
    return res


# 方法三：
def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res


nums = [1, 2, 3]
print(subsets1(nums))
