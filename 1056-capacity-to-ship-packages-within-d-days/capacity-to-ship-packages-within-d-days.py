def daysReq(weights:List[int], capacity:[int]) -> int:
    day = 1
    load = 0
    for wt in weights:
        if load+wt > capacity:
            day += 1
            load = wt
        else:
            load += wt
    return day

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low+high)//2
            if daysReq(weights,mid)<=days:
                high = mid-1
            else:
                low=mid+1
        return low

        