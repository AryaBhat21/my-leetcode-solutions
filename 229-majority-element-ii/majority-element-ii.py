class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Phase 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify candidates
        res = []
        target = len(nums) // 3
        
        for cand in [candidate1, candidate2]:
            if cand is not None and nums.count(cand) > target:
                res.append(cand)
                
        return res