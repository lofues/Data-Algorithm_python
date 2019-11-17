"""
    用回溯法解决正则表达式匹配  *匹配任意多个前一个字符 .匹配任意一个字符
"""
class Solution(object):
    def isMatch(self, s, p):
        # 若模式串匹配完毕  若主串结尾则结束
        if not p:return not s
        # 匹配当前一个字符
        first_match = True if s and p[0] in (s[0],'.') else False
        # 若是'*'则匹配当前一个或者不匹配
        if len(p) >= 2 and p[1] == '*':
            return (first_match and self.isMatch(s[1:],p)) or self.isMatch(s,p[2:])
        else:
            return first_match and self.isMatch(s[1:],p[1:])