class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        for i in s:
            if i=="(":
                st.append(")")
            elif i=="{":
                st.append("}")
            elif i=="[":
                st.append("]")
            elif len(st)==0 or st[-1]!=i:
                return False
            else:
                st.pop() 
       
        return len(st)==0

            
            
            
        