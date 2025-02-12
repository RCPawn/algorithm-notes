"""
LCP 33. 蓄水
    给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。
    小扣有以下两种操作：
    - 升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
    - 蓄水：将全部水桶接满水，倒入各自对应的水缸
    每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。
    注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。
    示例 1：
            输入：bucket = [1,3], vat = [6,8]
            输出：4
            解释： 第 1 次操作升级 bucket[0]； 第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。vat1.gif
    示例 2：
            输入：bucket = [9,0,1], vat = [0,2,2]
            输出：3
            解释： 第 1 次操作均选择升级 bucket[1] 第 2~3 次操作选择蓄水，即可完成蓄水要求。
"""
from typing import List


def storeWater(bucket: List[int], vat: List[int]) -> int:
    max_vat = max(vat)
    if max_vat == 0:
        return 0
    min_operations = float('inf')
    for i in range(1, max_vat + 1):  # i表示水桶容量每次增加1
        operations = 0  # 每次水桶容量升级后所需的操作次数
        # 遍历所有水缸
        for j in range(len(bucket)):
            # 如果当前水缸需要蓄水
            # 计算升级水桶所需的次数，首先计算水桶需要达到的容量，
            # 然后减去当前水桶的容量，确保操作次数不为负数
            operations += max(0, (vat[j] + i - 1) // i - bucket[j])

        # 更新最小操作次数
        # 对于当前水桶容量i，操作次数是当前蓄水操作次数 + 当前容量值i（即升级水桶的操作次数）
        min_operations = min(min_operations, operations + i)

    return min_operations


bucket = [1, 3]
vat = [6, 8]
print(storeWater(bucket, vat))
