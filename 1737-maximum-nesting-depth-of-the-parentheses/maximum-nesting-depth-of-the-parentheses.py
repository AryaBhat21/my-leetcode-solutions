class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        ans = 0

        for  i in s:
            if i=="(":
                st.append(i)
                ans = max(ans,len(st))
            elif i==")":
                st.pop()

        return ans
                
