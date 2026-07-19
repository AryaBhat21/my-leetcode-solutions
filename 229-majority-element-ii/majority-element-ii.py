class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count1, count2 = 0,0
        ele1, ele2 = None, None

        for i in range(len(nums)):
            if count1 == 0 and nums[i]!= ele2:
                count1 += 1
                ele1 = nums[i]

            elif count2 == 0 and nums[i]!= ele1:
                count2 += 1
                ele2 = nums[i]

            elif ele1 == nums[i]:
                count1 += 1
        
            elif ele2 == nums[i]:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

        res = []
        
        if ele1 is not None and nums.count(ele1) > len(nums)//3 :
            res.append(ele1)

        if ele2 is not None and nums.count(ele2) > len(nums)//3 :
            res.append(ele2)
         
        return res