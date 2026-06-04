class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        s = set(word)
        count = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in word and i.upper() in s:
                count+=1
        return count
            
        