class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for ch in s:
            if ch=="(":
                st.append(0)
            else:
                v = st.pop()
                st[-1]+=max(2*v,1)
        
        return st[0]
