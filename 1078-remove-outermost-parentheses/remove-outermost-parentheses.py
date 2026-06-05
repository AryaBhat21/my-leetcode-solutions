class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        res = ""

        for ch in s:
            if ch == "(":
                if st:
                    res+=ch
                st.append(ch)
            else:
                st.pop()
                if st:
                    res+=ch
        return res
        