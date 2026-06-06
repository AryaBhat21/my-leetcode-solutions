class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        st = []
        for i in num:
            while st and k>0 and st[-1]>i and len(num)!=1:
                k-=1
                st.pop()
            st.append(i)

        while k>0:
            k-=1
            st.pop()

        res = "".join(st).lstrip("0")
        return res if res else "0"
        