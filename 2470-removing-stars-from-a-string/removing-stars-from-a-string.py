class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for i in s:
            if i=="*":
                if not st:
                    break
                else:
                    st.pop()
            else:
                st.append(i)

        return "".join(st)

            
       

        