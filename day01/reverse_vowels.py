"""
345. 反转字符串中的元音字母
    给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
    元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
    示例 1：
            输入：s = "IceCreAm"
            输出："AceCreIm"
            解释：s 中的元音是 ['I', 'e', 'e', 'A']。反转这些元音，s 变为 "AceCreIm".
    示例 2：
            输入：s = "leetcode"
            输出："leotcede"
"""


def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return ''.join(s)


string = "IceCreAm"
print(reverseVowels(string))
