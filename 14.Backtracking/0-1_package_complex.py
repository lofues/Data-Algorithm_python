"""
    回溯算法解决0-1背包升级版 每个物品除了有重量还有价值
"""


class Solution:
    def solution(self,ws,vs,w):
        # w 是背包承重量 ws 为物品重量数组 vs 为物品价值数组
        n = len(ws)
        max_v = float('-inf')

        def helper(cw,cv,n,i):
            # 如果背包已背满或者已经遍历完所有物品则退出
            nonlocal max_v
            if cw == w or i == n:
                if cv > max_v:max_v = cv
                return
            # 选择不背此物品或者背此物品
            helper(cw,cv,n,i+1)
            if cw + ws[i] <= w:
                helper(cw+ws[i],cv+vs[i],n,i+1)
        helper(0,0,n,0)
        return max_v

a = Solution()
print(a.solution([2,2,4,6,3],[3,4,8,9,6],9))