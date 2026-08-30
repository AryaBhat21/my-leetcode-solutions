def sum_d(arr:List[int], d:int)->int:
    sum_val = 0
    for i in arr:
        sum_val+=(ceil(i/d))
    return sum_val

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums)>threshold:
            return -1
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            if sum_d(nums,mid)<=threshold:
                high = mid-1
            else: 
                low = mid+1
        return low 