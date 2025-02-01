"""
350. 两个数组的交集 II
    给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
    返回结果中每个元素出现的次数，
    应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
    可以不考虑输出结果的顺序。
    示例 1：
            输入：nums1 = [1,2,2,1], nums2 = [2,2]
            输出：[2,2]
    示例 2:
            输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
            输出：[4,9]
"""
import collections
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    list1 = list(nums1)
    res_list = list()
    for num in nums2:
        if list1.__contains__(num):
            res_list.append(num)
            list1.remove(num)
    return res_list


def intersect1(nums1: List[int], nums2: List[int]) -> List[int]:
    map1 = {}
    res = []
    for num in nums1:
        map1[num] = map1.get(num, 0) + 1
    for num in nums2:
        if map1.get(num, 0) > 0:
            res.append(num)
            map1[num] -= 1
    return res


def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        return self.intersect2(nums2, nums1)
    m = collections.Counter()
    for num in nums1:
        m[num] += 1
    res = list()
    for num in nums2:
        if (m.get(num, 0)) > 0:
            res.append(num)
            m[num] -= 1
            if m[num] == 0:
                m.pop(num)
    return res


def intersect3(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    length1, length2 = len(nums1), len(nums2)
    res = list()
    index1 = index2 = 0
    while index1 < length1 and index2 < length2:
        if nums1[index1] < nums2[index2]:
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        else:
            res.append(nums1[index1])
            index1 += 1
            index2 += 1
    return res


arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersect(arr1, arr2))
