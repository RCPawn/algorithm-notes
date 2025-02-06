"""
997. 找到小镇的法官
    小镇里有 n 个人，按从 1 到 n 的顺序编号。
    传言称，这些人中有一个暗地里是小镇法官。
    如果小镇法官真的存在，那么：
    1. 小镇法官不会信任任何人。
    2. 每个人（除了小镇法官）都信任这位小镇法官。
    3. 只有一个人同时满足属性 1 和属性 2 。
    给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
    如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
    示例 1：
            输入：n = 2, trust = [[1,2]]
            输出：2
    示例 2：
            输入：n = 3, trust = [[1,3],[2,3]]
            输出：3
    示例 3：
            输入：n = 3, trust = [[1,3],[2,3],[3,1]]
            输出：-1
"""
from collections import Counter


# 方法一：
def findJudge(n, trust):
    trust_count = [0] * (n + 1)
    trust_others = [0] * (n + 1)

    for a, b in trust:
        trust_count[a] += 1
        trust_others[b] += 1

    # answer is in [1, n]
    for i in range(1, n + 1):
        if (trust_count[i] == n - 1
                and trust_others[i] == 0):
            return i

    return -1


# 方法二：
def findJudge1(n, trust):
    in_degrees = Counter(a for a, _ in trust)
    out_degrees = Counter(b for _, b in trust)
    return next((i for i in range(1, n + 1)
                 if in_degrees[i] == n - 1
                 and out_degrees[i] == 0), -1)


trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
print(findJudge(4, trust))
