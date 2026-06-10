class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for ch in chars:
            d[ch] = d.get(ch, 0) + 1
        res = 0
        flag = False
        for word in words:
            t = {}
            for ch in word:
                t[ch] = t.get(ch, 0) + 1
            flag = True
            for ch in t:
                if t[ch] > d.get(ch, 0):
                    flag = False
                    break
            if flag:
                res += len(word)
        return res