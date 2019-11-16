"""
    回溯算法解决正则匹配   *匹配一个或多个   .匹配任意一个
"""


class Solution:
    def __init__(self):
        self.match = False

    def solution(self,String,pattern):
        s_len = len(String)
        p_len = len(pattern)
        self.match = False
        self._solution(String,pattern,0,0,s_len,p_len)
        return self.match

    def _solution(self,String,pattern,s_cur,p_cur,s_len,p_len):
        if self.match is True:return
        if p_len == p_cur:
            if s_cur == s_len:
                self.match = True
            return
        if pattern[p_cur] == '*':
            # *匹配0或者多个  因此从0开始遍历
            for k in range(s_len-s_cur+1):
                self._solution(String,pattern,s_cur+k,p_cur+1,s_len,p_len)
        elif pattern[p_cur] == '.':
            # 匹配0 或者1个
            self._solution(String,pattern,s_cur+1,p_cur+1,s_len,p_len)
            self._solution(String,pattern,s_cur,p_cur+1,s_len,p_len)
        elif s_cur < s_len and String[s_cur] == pattern[p_cur]:
            self._solution(String,pattern,s_cur+1,p_cur+1,s_len,p_len)




