def dig_sum(val:int)->int:
    dig = 0 
    while val>0:
        dig = dig + val%10
        val = val//10
    return dig 
    

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum_dig = dig_sum(nums[i])
            if i==sum_dig:
                return i
        return -1