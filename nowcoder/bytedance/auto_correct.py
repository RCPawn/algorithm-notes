"""
    实现一个自动校对程序，修复字符串中的拼写错误。规则如下：
    1. 三个相同字母连在一起：去掉一个字母。例如，helllo -> hello。
    2. 两对相同字母（AABB型）连在一起：去掉第二对的一个字母。例如，helloo -> hello。
    3. 优先从左到右匹配：例如，AABBCC 应优先修复 AABB，结果为 AABCC。
    输入：
        第一行：整数 N，表示待校验的字符串数量。
        接下来 N 行：每行一个待校验的字符串。
    输出：
        N 行：每行一个修复后的字符串。
    示例：
        输入：
            2
            helloo
            wooooooow
        输出：
            hello
            woow
"""


# N = int(input())
#
# for _ in range(N):
#     res = []
#     s = input()
#     if len(s) < 3:
#         print(s)
#     else:
#         for i in range(len(s)):
#             res.append(s[i])
#             if len(res) >= 3 and res[-1] == res[-2] == res[-3]:
#                 res.pop()
#             if len(res) >= 4 and res[-1] == res[-2] and res[-3] == res[-4]:
#                 res.pop()
#         print(''.join(res))

def main():
    N = int(input())
    for _ in range(N):
        s = input().strip()
        res = []
        for c in s:
            # 如果最后两个字符和当前字符相同，则会形成三个相同的字符，跳过当前字符
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            # 如果最后一个字符和当前字符相同，并且再往前两个字符也构成一对，则形成两个连续的对子，跳过当前字符
            if len(res) >= 3 and res[-1] == c and res[-2] == res[-3]:
                continue
            res.append(c)
        print(''.join(res))


if __name__ == '__main__':
    main()
