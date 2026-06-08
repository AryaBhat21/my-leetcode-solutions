class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        found = False
        while low<=high:
            mid = (low+high)//2
            if target == nums[mid]:
                found = True
                return mid                
            elif target>nums[mid]:
                low = mid +1
            else:
                high = mid-1

        if not found:
            return -1
        