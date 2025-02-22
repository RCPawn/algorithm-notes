"""
    小红拿到了一个长度为 n 的，仅包含小写字母的字符串 str，
    请你取出所有长度恰好为 2 的连续子串，并将它们按字典序升序输出。

    字典序的定义：
        两个字符串 s 和 t，从左到右数第一个不相同的字符，
        ASCII 码更小的字符所属的字符串字典序更小。
        例如："ab" 的字典序小于 "ca"。

    输入：
        一个仅包含小写字母的字符串 str。字符串长度不超过 100000。

    输出：
        输出 n-1 行，每行输出一个长度为 2 的连续子串，按字典序升序排序。

    示例：
        输入：
            ababa
        输出：
            ab
            ab
            ba
            ba
"""

s = input().strip()
substrings = []

for i in range(len(s) - 1):
    substrings.append(s[i:i + 2])

substrings.sort()
for sub in substrings:
    print(sub)
