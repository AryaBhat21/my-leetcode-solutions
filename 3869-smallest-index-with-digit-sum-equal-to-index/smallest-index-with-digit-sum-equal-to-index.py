# def dig_sum(val:int)->int:
#     dig = 0 
#     while val>0:
#         dig = dig + val%10
#         val = val//10
#     return dig 
    

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i==sum(int(d) for d in str(num)):
                return i
        return -1