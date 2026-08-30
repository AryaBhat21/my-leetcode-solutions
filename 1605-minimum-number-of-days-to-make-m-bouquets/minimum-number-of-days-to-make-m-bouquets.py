def posDays(arr: List[int], day:int, m:int, k:int)-> bool:
        count = 0
        no_boq = 0
        
        for i in arr:
            if i<=day:
                count+=1
            else:
                no_boq+=(count//k)
                count = 0
        no_boq+=count//k
        if no_boq>=m:
            return True
        else:
            return False

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans=-1
        while low<=high:
            mid = (low+high)//2
            if posDays(bloomDay,mid,m,k):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 