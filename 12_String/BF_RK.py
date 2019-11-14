"""
    实现BF：暴力匹配
    RK：hash比较
"""


def bf(s,t):
    # 匹配成功返回下标否则返回-1
    if len(s) < len(t):return -1
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i+j] != t[j]:break
            else:
                if j == len(t) - 1:return i
    return -1


def rk(s,t):
    # 对每个len(t)长度的s子串的hash值与t的hash值比较
    # 可以优化为：将所有字符范围假设为k统计后设为k进制，hash算法是将k进制的数转换为10进制数
    # 可以将k进制的m(->len(t))次方结果保存在数组中不用重复计算，此外，每个主串中的模式串相邻之间有关系
    if len(s) < len(t):
        return -1
    temp = hash(t)
    length = len(t)
    for i in range(len(s)-length+1):
        cur = s[i:i+length]
        if hash(cur) == temp:
            return i
    return -1

print(bf('bba','a'))
print(rk('bbabbb','ba'))