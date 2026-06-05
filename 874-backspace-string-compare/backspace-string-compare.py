class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def fun(str):
            st = []

            for ch in str:
                if ch != "#":
                    st.append(ch)
                elif st and ch=="#":
                    st.pop()
                      
            return "".join(st)
        return fun(s)==fun(t)   