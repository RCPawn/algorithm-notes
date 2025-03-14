"""
32. 最长有效括号
    给你一个只包含 '(' 和 ')' 的字符串，找
    出最长有效（格式正确且连续）括号子串的长度。
    示例 1：
            输入：s = "(()"
            输出：2
            解释：最长有效括号子串是 "()"
    示例 2：
            输入：s = ")()())"
            输出：4
            解释：最长有效括号子串是 "()()"
    示例 3：
            输入：s = ""
            输出：0
"""


def longestValidParentheses(s: str) -> int:
    if not s:
        return 0

    dp = [0] * len(s)
    max_len = 0

    for i in range(1, len(s)):
        if s[i] == ')':  # 只有遇到 ')' 才有可能构成有效括号
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
            max_len = max(max_len, dp[i])

    return max_len


s = ")()())"
print(longestValidParentheses(s))
