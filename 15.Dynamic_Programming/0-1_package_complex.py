"""
    用动态规划解决0-1 背包问题  每个物品不仅拥有重量 还有价值
"""


class Solution:
    def solution(self,ws,vs,w):
        # 申请所有物品所有重量的二维数组 其中存储价值
        n = len(ws)
        states = [[-1 for _ in range(w+1)] for i in range(n)]
        states[0][0] = 0
        if ws[0] <= w:states[0][ws[0]] = vs[0]
        # 遍历从第二个开始的所有物品
        # 分为装下该物品与不装下该物品
        for i in range(1,n):
            # 不装下该物品
            for j in range(0,w+1):
                if states[i-1][j] >= 0:states[i][j] = states[i-1][j]
            # 装下该物品
            for j in range(0,w-ws[i]+1):
                if states[i-1][j] >= 0:
                    v = states[i-1][j] + vs[i]
                    # 在装下该物品的状态下取最大值
                    if v > states[i][j+ws[i]]:states[i][j+ws[i]] = v
        max_v = float('-inf')
        for j in range(w+1):
            if states[i-1][j] > max_v:max_v = states[i-1][j]
        return max_v

a = Solution()
print(a.solution([2,2,4,6,3],[3,4,8,9,6],9))
