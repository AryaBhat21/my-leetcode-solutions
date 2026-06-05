class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st =[]
        for i in s:
            if st and abs((ord(st[-1])-ord(i)))==0:
            #if st and st[-1]!=i andd st[-1].lower()==i.lower():
                st.pop()
            else:
                st.append(i)
        return "".join(st)
