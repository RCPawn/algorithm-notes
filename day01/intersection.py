"""
349. 两个数组的交集
    给定两个数组 nums1 和 nums2 ，返回 它们的交集。
    输出结果中的每个元素一定是 唯一 的。
    我们可以 不考虑输出结果的顺序。
    示例 1：
            输入：nums1 = [1,2,2,1], nums2 = [2,2]
            输出：[2]
    示例 2：
            输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
            输出：[9,4]
            解释：[4,9] 也是可通过的
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    res_list = list()
    for num in nums2:
        if set1.__contains__(num):
            res_list.append(num)
            set1.remove(num)
    return res_list


def intersection1(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
