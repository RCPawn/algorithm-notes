"""
46. 全排列
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。
    你可以 按任意顺序 返回答案。
    示例 1：
            输入：nums = [1,2,3]
            输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    示例 2：
            输入：nums = [0,1]
            输出：[[0,1],[1,0]]
    示例 3：
            输入：nums = [1]
            输出：[[1]]
"""
from typing import List


# 方法一：
def permute(nums: List[int]) -> List[List[int]]:
    res = []
    used = [False] * len(nums)

    def backtrack(path: List):
        n = len(nums)
        if len(path) == n:
            res.append(path.copy())
            return

        for i in range(n):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return res


# 方法二：
def permute1(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start: int):
        n = len(nums)
        if start == n:
            res.append(nums[:])
            return

        for i in range(start, n):
            # 交换当前元素到 start 位置
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            # 回溯：交换回去以恢复原数组
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return res


nums = [1, 2, 3]
print(permute1(nums))
