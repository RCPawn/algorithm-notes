"""
1385. 两个数组间的距离值
    给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
    「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，
    不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
    示例 1：
            输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
            输出：2
    示例 2：
            输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
            输出：2
    示例 3：
            输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
            输出：1
"""
import bisect
from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    count = 0
    for num1 in arr1:
        is_valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                is_valid = False
                break
        if is_valid:
            count += 1
    return count


def findTheDistanceValue1(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    count = 0
    for e in arr1:
        p = bisect.bisect_left(arr2, e)
        if p == len(arr2) or abs(e - arr2[p]) > d:
            if p == 0 or abs(e - arr2[p - 1]) > d:
                count += 1
    return count


arr1 = [1, 4, 2, 3]
arr2 = [-4, -3, 6, 10, 20, 30]

print(findTheDistanceValue(arr1, arr2, 3))
