class Solution:
    def solveNQueens(self, n: int):
        self.ans = []

        def recur(position: list, row: int) -> int:
            if row==n:
                temp = []
                for i in range(n):
                    temp.append('.'*position[i]+'Q'+'.'*(n-1-position[i]))
                self.ans.append(temp)
            else:
                for col in range(n):
                    if is_value(position,row,col): recur(position+[col],row+1)

        def is_value(position,row,col):
            for i in range(row):
                if position[i] in {col,col+(row-i),col-(row-i)}: return False
            else: return True

        def print_ans():
            for i in self.ans:
                for row in i:
                    print(row)
                print('')
        recur([],0)
        print_ans()

test = Solution()
test.solveNQueens(5)
