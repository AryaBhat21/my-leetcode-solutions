class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_2 = len(nums)//2
        
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1

        maj = 0

        for i in freq:
            if freq[i]>n_2 and freq[i]>maj:
                maj = i

        return maj

        