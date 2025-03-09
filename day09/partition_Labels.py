"""
763. 划分字母区间
    给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
    例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，
    但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
    注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
    返回一个表示每个字符串片段的长度的列表。
    示例 1：
            输入：s = "ababcbaca defegdehijhklij"
            输出：[9,7,8]
            解释：划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
                每个字母最多出现在一个片段中。
                像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
    示例 2：
            输入：s = "eccbbbbdec"
            输出：[10]
"""
from typing import List


def partitionLabels(s: str) -> List[int]:
    # 记录每个字符最后出现的位置
    last = {c: i for i, c in enumerate(s)}
    start = end = 0
    result = []

    for i, c in enumerate(s):
        # 更新当前区间的右边界
        end = max(end, last[c])
        # 到达当前区间的最右边
        if i == end:
            result.append(i - start + 1)
            # 更新下一区间的起始位置
            start = i + 1

    return result


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
