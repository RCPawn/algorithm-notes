"""
541. 反转字符串 II
    给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
    示例 1：
            输入：s = "abcdefg", k = 2
            输出："bacdfeg"
    示例 2：
            输入：s = "abcd", k = 2
            输出："bacd"
"""


# 方法一：
def reverseStr(s: str, k: int) -> str:
    # 将字符串转为列表，因为字符串是不可变的
    s = list(s)
    n = len(s)
    for i in range(0, n, 2 * k):
        l, r = i, min(n - 1, i + k - 1)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return ''.join(s)


# 方法二：
def reverseStr1(s: str, k: int) -> str:
    # 将字符串转为列表，因为字符串是不可变的
    s = list(s)
    for i in range(0, len(s), 2 * k):
        # s[i:i + k] = s[i:i + k][::-1]
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)


# 示例1
# 输出: "bacdfeg"
print(reverseStr("abcdefg", 2))

# 示例2
# 输出: "bacd"
print(reverseStr("abcd", 2))
