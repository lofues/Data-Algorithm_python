"""
    回溯算法解决八皇后问题
"""
class EightQueen:
    def __init__(self,capacity):
        self.queen = [-1 for _ in range(capacity)]

    def solution(self):
        # 调用递归函数依次计算每一行的皇后位置
        self._solution(0)

    def _solution(self,row):
        if row == len(self.queen):
            self.printf()
            return
        for column in range(len(self.queen)):
            if self.is_ok(row,column):
                self.queen[row] = column
                self._solution(row+1)


    def is_ok(self,row,col):
        leftup,rightup = col-1,col+1
        for height in range(row-1,-1,-1):
            if leftup >= 0:
                if self.queen[height] == leftup:return False
            if rightup < len(self.queen):
                if self.queen[height] == rightup:return False
            if self.queen[height] == col:return False
            leftup -= 1
            rightup += 1
        return True

    def printf(self):
        print(self.queen)
        for height in range(len(self.queen)):
            print('#'*(self.queen[height]) + 'Q' + '#'*(len(self.queen)-self.queen[height]-1))

a = EightQueen(10)
a.solution()

