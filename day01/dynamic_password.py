"""
LCR 182. 动态口令
    某公司门禁密码使用动态口令技术。
    初始密码为字符串 password，密码更新均遵循以下步骤：
    设定一个正整数目标值 target
    将 password 前 target 个字符按原顺序移动至字符串末尾
    请返回更新后的密码字符串。
        示例 1：
                输入: password = "s3cur1tyC0d3", target = 4
                输出: "r1tyC0d3s3cu"
        示例 2：
                输入: password = "lrloseumgh", target = 6
                输出: "umghlrlose"
"""


def dynamic_password(s: str, n: int) -> str:
    return s[n:] + s[:n]


password = "s3cur1tyC0d3"
target = 4
print(dynamic_password(password, target))
