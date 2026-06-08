class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        first=-1
        last=-1

        while low<=high:
            mid = (low+high)//2

            if target == nums[mid]:
                first = mid
                high = mid -1
                
            elif target>nums[mid]:
                low = mid+1
                        
            else:
                high = mid-1

        if first==-1:
            return [-1,-1]

        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if target == nums[mid]:
                last = mid
                low = mid + 1
                
            elif target>nums[mid]:
                low = mid+1
                        
            else:
                high = mid-1


        return [first,last]


            

        