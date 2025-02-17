"""
1668. 最大重复子字符串
    给你一个字符串 sequence ，
    如果字符串 word 连续重复 k 次
    形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。
    单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。
    如果 word 不是 sequence 的子串，那么重复值 k 为 0 。
    给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。
    示例 1：
            输入：sequence = "ababc", word = "ab"
            输出：2
            解释："abab" 是 "ababc" 的子字符串。
    示例 2：
            输入：sequence = "ababc", word = "ba"
            输出：1
            解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
    示例 3：
            输入：sequence = "ababc", word = "ac"
            输出：0
            解释："ac" 不是 "ababc" 的子字符串。
"""


# 方法一：
def max_repeating(sequence, word):
    max_count = 0
    n = len(sequence)
    m = len(word)
    for i in range(n):
        count = 0
        while sequence[i:i + m] == word:
            count += 1
            i += m
        max_count = max(max_count, count)
    return max_count


# 方法二：
def max_repeating1(sequence, word):
    n, m = len(sequence), len(word)
    dp = [0] * (n + 1)
    max_count = 0
    # 从后往前遍历 n - m ~ 0
    for i in range(n - m, -1, -1):
        if sequence[i:i + m] == word:
            dp[i] = dp[i + m] + 1
            max_count = max(max_count, dp[i])
        else:
            dp[i] = 0
    return max_count


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
print(max_repeating1(sequence, word))
