class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        # st = []
        # l = list(s)
        # for i in l:
        #     if i.isupper():
        #         if st and i.lower()==st[-1].lower():
        #             st.pop()
        #     else:
        #         st.append(i)
        # return "".join(st)
        st =[]
        for i in s:
            if st and abs((ord(st[-1])-ord(i)))==32:
                st.pop()
            else:
                st.append(i)
        return "".join(st)

        