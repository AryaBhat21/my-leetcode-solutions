class Solution:
    def rowval(self, row:int) -> List[int]:
        ans = 1
        ansRow = []
        ansRow.append(ans)

        for col in range(1, row):
            ans = (ans * (row-col))/col
            ansRow.append(int(ans))
        
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(1, numRows+1):
            ans.append(self.rowval(row))

        return ans

        