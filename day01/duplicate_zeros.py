"""
1089. 复写零
    给你一个长度固定的整数数组 arr ，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
    注意：请不要在超过该数组长度的位置写入元素。
    请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
    示例 1：
            输入：arr = [1,0,2,3,0,4,5,0]
            输出：[1,0,0,2,3,0,0,4]
            解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
    示例 2：
            输入：arr = [1,2,3]
            输出：[1,2,3]
            解释：调用函数后，输入的数组将被修改为：[1,2,3]
"""
from typing import List


# 方法一：
def duplicateZeros(arr: List[int]) -> None:
    n = len(arr)
    count = 0
    for e in arr:
        if e == 0:
            count += 1
    i = n - 1
    j = n + count - 1
    while i >= 0:
        if arr[i] == 0:
            if j < n:
                arr[j] = 0
            j -= 1
        if j < n:
            arr[j] = arr[i]
        i -= 1
        j -= 1


# 方法二：
def duplicateZeros1(arr: List[int]) -> None:
    n = len(arr)
    top = 0
    i = -1
    while top < n:
        i += 1
        top += 1 if arr[i] else 2
    j = n - 1
    if top == n + 1:
        arr[j] = 0
        j -= 1
        i -= 1
    while j >= 0:
        arr[j] = arr[i]
        j -= 1
        if arr[i] == 0:
            arr[j] = arr[i]
            j -= 1
        i -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)
print(arr)
