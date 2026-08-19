from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res_map = defaultdict(set)
        for row,col in reservedSeats:
            if 1<col<10:
                res_map[row].add(col)
        ans = 2*n
        left = {2,3,4,5}
        mid = {4,5,6,7}
        right = {6,7,8,9}

        for cols in res_map.values():
            left_ok = left.isdisjoint(cols)
            mid_ok = mid.isdisjoint(cols)
            right_ok = right.isdisjoint(cols)

            if left_ok and right_ok:
                continue
            elif left_ok or right_ok or mid_ok:
                ans -= 1
            else:
                ans -= 2   
        return ans        



