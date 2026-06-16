class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        j = len(numbers)

        while i<j:
            curr = numbers[j-1] + numbers[i-1]

            if curr == target:
                return [i,j]

            if curr < target:
                i+=1
            else:
                j-=1

               



