"""
    使用回溯算法解决N皇后问题
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 0:
            return
        ans = []
        queen = [-1 for _ in range(n)]
        self.queen_row(0, queen, ans)
        return ans

    def queen_row(self, row, queen, ans):
        if row == len(queen):
            self.add_queen(queen, ans)
            return
        else:
            for column in range(len(queen)):
                if self.is_ok(queen, row, column):
                    queen[row] = column
                    self.queen_row(row + 1, queen, ans)

    def is_ok(self, queen, row, col):
        leftup, rightup = col - 1, col + 1
        for height in range(row - 1, -1, -1):
            if queen[height] == col: return False
            if leftup >= 0:
                if queen[height] == leftup: return False
            if rightup < len(queen):
                if queen[height] == rightup: return False
            leftup -= 1
            rightup += 1
        return True

    def add_queen(self, queen, ans):
        temp = []
        for length in queen:
            temp.append('.' * length + 'Q' + '.' * (len(queen) - length - 1))
        ans.append(temp)