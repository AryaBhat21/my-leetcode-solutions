class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        st = []

        for ch in s:
            if ch ==")":
                res = []
                while st[-1] != "(":
                    res.append(st.pop())
                st.pop()
                st.extend(res)
            else:
                st.append(ch)

        return "".join(st)


        