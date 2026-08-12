class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=1
        ansR = []
        ansR.append(1)
        for c in range(1,rowIndex+1):
            ans = ans * (rowIndex-c+1)
            ans = ans//c
            ansR.append(ans)
        return ansR