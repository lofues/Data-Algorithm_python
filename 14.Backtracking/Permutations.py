"""
    用回溯算法解决全排列问题   例如给出 N (N>2) 求出k个元素的全排列
    列如 N = 3, k = 2
    [[1,2],[1,3],[2,3]]
"""

class Solution:
    def solution(self,n,k):
        if n < k:return
        ret = []

        def helper(n,k,index,ans,ret):
            if k == 0:
                ret.append(ans)
                return
            for cur in range(index,n+1):
                helper(n,k-1,cur+1,ans+[cur],ret)
        helper(n,k,1,[],ret)
        return ret


a = Solution()
print(a.solution(4,2))