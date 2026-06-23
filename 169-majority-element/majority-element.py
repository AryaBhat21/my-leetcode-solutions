class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = None

        for i in nums:
            if count == 0:
                ele = i
                count += 1
            elif i==ele:
                count+=1 
            else:
                count-=1 
        
        if nums.count(ele)>(len(nums)//2):
            return ele

        return -1

        