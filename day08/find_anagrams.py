"""
438. 找到字符串中所有字母异位词
    给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，
    返回这些子串的起始索引。不考虑答案输出的顺序。
    示例 1:
            输入: s = "cbaebabacd", p = "abc"
            输出: [0,6]
            解释:
                起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
                起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
     示例 2:
            输入: s = "abab", p = "ab"
            输出: [0,1,2]
            解释:
                起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
                起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
                起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""
from typing import List


# 超出时间限制
def findAnagrams(s: str, p: str) -> List[int]:
    res = []
    n = len(p)
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if sorted(substr) == sorted(p):
            res.append(i)
    return res


# 滑动窗口
def find_anagrams(s, p):
    m, n = len(p), len(s)
    if m > n:
        return []

    res = []
    p_count = [0] * 26
    s_count = [0] * 26

    for c in p:
        p_count[ord(c) - ord('a')] += 1

    for i in range(n):
        s_count[ord(s[i]) - ord('a')] += 1
        if i >= m:
            s_count[ord(s[i - m]) - ord('a')] -= 1
        if s_count == p_count:
            res.append(i - m + 1)

    return res


print(find_anagrams("cbaebabacd", "abc"))
