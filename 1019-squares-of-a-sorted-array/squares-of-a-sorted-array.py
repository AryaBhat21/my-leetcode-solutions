class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pos = n-1 
        large = 0
        left = 0
        right = n-1

        while pos>=0:
            if nums[left]*nums[left] > nums[right]*nums[right]:
                large = nums[left]*nums[left]
                left +=1
            else:
                large = nums[right]*nums[right]
                right -= 1
        
            res[pos]=large
            pos-=1

        return res
