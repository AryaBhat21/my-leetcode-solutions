class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        s = sentence.split()
        vowel = "aeiouAEIOU"
        res = []
        c=1
        for i in range(len(s)):
            word = s[i]
            if word[0] in vowel:
                res.append(word+"ma"+"a"*c)
                c+=1
            
            else:
                res.append(word[1:]+word[0]+"ma"+"a"*c)
                c+=1
        return " ".join(res)
            