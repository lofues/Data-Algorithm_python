"""
    使用动态规划求解0 1 背包问题
    记录每一个物品时的状态
"""

class Solution:
    # ws 表示物品的重量 w 表示背包的最大承重量
    # solution_1  申请所有物品的所有重量的重量数组
    def solution(self,ws,w):
        # 申请每个物品的状态数组
        n = len(ws)
        states = [[False for _ in range(w+1)] for i in range(n)]
        states[0][0] = True
        if ws[0] <= w:states[0][ws[0]] = True
        # 表示每一个可能的状态  以及状态的转移
        for i in range(1,n):
            for j in range(w+1):
                # 遍历前一个物品的所有状态  如果加上当前物品的重量仍然小于等于w  就放入背包
                if states[i-1][j] is True:
                    if j + ws[i] <= w:
                        states[i][j+ws[i]] = True
                # 如果加上当前物品的重量大于w  就不放入背包
                    else:
                        states[i][j] = True
        for j in range(w,-1,-1):
            if states[n-1][j] is True:
                return j

    # solution_2  只需要申请所有重量的一维数组
    def solution_2(self,ws,w):
        n = len(ws)
        states = [False for _ in range(w+1)]
        states[0] = True
        if ws[0] <= w:
            states[ws[0]] = True
        for i in range(1,n):
            # 从后往前遍历  如果可以装入ws[i] 就装入
            for j in range(w-ws[i],-1,-1):
                if states[j] is True:states[j+ws[i]] = True
        for i in range(len(states)-1,-1,-1):
            if states[i] is True:return i

a = Solution()
print(a.solution([7,8,8,6],5))
print(a.solution_2([1,2,3,4],5))
