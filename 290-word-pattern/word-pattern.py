class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        w = s.split()
        if len(p) != len(w):
            return False
        d1 = {}
        d2 = {}

        for i in range(len(p)):
            if p[i] in d1:

                if d1[p[i]] != w[i]:
                    return False
            else:
                d1[p[i]] = w[i]

            if w[i] in d2:

                if d2[w[i]] != p[i]:
                    return False
            else:
                d2[w[i]] = p[i]

        return True
        