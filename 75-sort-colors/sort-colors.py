class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = nums.count(0)
        cnt1 = nums.count(1)
        cnt2 = nums.count(2)

        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0, cnt0+cnt1):
            nums[i]=1
        for i in range(cnt1+cnt0, len(nums)):
            nums[i]=2

