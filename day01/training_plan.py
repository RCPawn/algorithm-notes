"""
LCR 139. 训练计划 I
    教练使用整数数组 actions 记录一系列核心肌群训练项目编号。
    为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。
    请将调整后的训练项目编号以 数组 形式返回。
    示例 1：
            输入：actions = [1,2,3,4,5]
            输出：[1,3,5,2,4]
            解释：为正确答案之一
"""
from typing import List


def training_plan(actions: List) -> List[int]:
    l, r = 0, len(actions) - 1
    while l < r:
        if actions[l] % 2 == 0 and actions[r] % 2 != 0:
            actions[l], actions[r] = actions[r], actions[l]
        if actions[l] % 2 != 0:
            l += 1
        if actions[r] % 2 == 0:
            r -= 1
    return actions


arr = [1, 2, 3, 4, 5]
print(training_plan(arr))
