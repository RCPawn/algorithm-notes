"""
    496. 下一个更大元素 I
        nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
        给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
        对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
        如果不存在下一个更大元素，那么本次查询的答案是 -1 。
        返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
        示例 1：
                输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
                输出：[-1,3,-1]
                解释：nums1 中每个值的下一个更大元素如下所述：
                - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
                - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
                - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
        示例 2：
                输入：nums1 = [2,4], nums2 = [1,2,3,4].
                输出：[3,-1]
                解释：nums1 中每个值的下一个更大元素如下所述：
                - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
                - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
"""


# 方法一：
def nextGreaterElement(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        n = len(nums2)
        index = -1
        for j in range(n):
            if nums1[i] == nums2[j]:
                index = j
                break
        next_greater = -1
        for k in range(index + 1, n):
            if nums2[k] > nums1[i]:
                next_greater = nums2[k]
                break
        res.append(next_greater)
    return res


# 方法二：
def nextGreaterElement1(nums1, nums2):
    res = []
    for num in nums1:
        index = nums2.index(num)
        next_greater = -1
        for i in range(index + 1, len(nums2)):
            if nums2[i] > num:
                next_greater = nums2[i]
                break
        res.append(next_greater)
    return res


# 方法三:
def nextGreaterElement2(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    while stack:
        next_greater[stack.pop()] = -1

    return [next_greater[num] for num in nums1]


# 示例 1
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement2(nums1, nums2))  # 输出: [-1, 3, -1]

# 示例 2
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement2(nums1, nums2))  # 输出: [3, -1]
