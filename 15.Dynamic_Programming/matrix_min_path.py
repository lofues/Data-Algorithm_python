"""
    有一个矩阵w[n][n] 求从(0,0) 到 (n-1,n-1) 的最短距离
    要求每个节点只能向又和向下走
"""
import time


def back_track(m,n):
    # 先使用回溯算法求解
    min_dist = float('inf')
    def helper(i,j,dist):
        nonlocal min_dist
        if i == m or j == n:
            return
        if i == m-1 and j == n-1:
            if dist < min_dist:min_dist = dist
            return
        elif i == m-1:
            helper(i,j+1,dist+1)
        elif j == n-1:
            helper(i+1,j,dist+1)
        else:
            helper(i, j + 1, dist + 1)
            helper(i + 1, j, dist + 1)
    helper(0,0,0)
    return min_dist

def dp(m,n):
    static = [[0 for _ in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:static[i][j] = min(static[i-1][j],static[i][j-1]) + 1
            elif i > 0:static[i][j] = static[i-1][j] + 1
            elif j > 0:static[i][j] = static[i][j-1] + 1
    print(static)
    return static[m-1][n-1]

# backtracking time cost
start = time.time()
print(back_track(15,10))
end = time.time()
print('backtracking cost:',end-start)

# dynamic programming cost
start = time.time()
print(dp(15,10))
end = time.time()
print('dynamic programming cost:',end-start)