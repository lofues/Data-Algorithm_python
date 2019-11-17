"""
    用回溯法实现0-1背包问题
    w 为背包最大承重量，nums 为各个石块的重量，求最大承重量

    每个石块都可以选择装或者不装，因此要有装或者不装两个分支并在每个分支判断大小，若遍历到最后以及背包已满就返回
"""


class Solution:
    _max = float('-inf')

    def solution(self,w,nums):
        def helper(w,nums,i,cur_weight):
            if cur_weight == w or i >= len(nums):
                if cur_weight >= self._max:
                    self._max = cur_weight
                return
            helper(w,nums,i+1,cur_weight)
            if cur_weight + nums[i] <= w:
                helper(w,nums,i+1,cur_weight + nums[i])
        helper(w,nums,0,0)
        return self._max


a = Solution()
print(a.solution(100,[10,20,30,110,30]))