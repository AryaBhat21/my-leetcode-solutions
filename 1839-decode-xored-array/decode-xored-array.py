class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        for i in range(len(encoded)+1):
            if i == 0:
                encoded.insert(0, first)
            else:
                encoded[i]=encoded[i]^encoded[i-1]

        return encoded

        