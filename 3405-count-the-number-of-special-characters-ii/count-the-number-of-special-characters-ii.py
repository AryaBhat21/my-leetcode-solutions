class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l = {}
        u = {}
        c = 0
        for i , ch in enumerate(word):
            if ch.islower():
                l[ch] = i
            elif ch not in u:
                u[ch] = i
        for ch in l:
            if ch.upper() in u:
                if l[ch] < u[ch.upper()]:
                    c += 1
        
        return c
        