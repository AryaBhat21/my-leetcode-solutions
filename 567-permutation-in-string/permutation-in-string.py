class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count = {}
        for i in s1:
            s1_count[i] = s1_count.get(i, 0) + 1

        win_count = {}
        l = 0

        for r in range(len(s2)):
            char_right = s2[r]
            win_count[char_right] = win_count.get(char_right,0)+1

            if (r-l+1) > len(s1):
                char_left = s2[l]
                win_count[char_left] -= 1

                if win_count[char_left] == 0:
                    del win_count[char_left]
                
                l+=1

            if win_count == s1_count:
                return True
        
        return False

