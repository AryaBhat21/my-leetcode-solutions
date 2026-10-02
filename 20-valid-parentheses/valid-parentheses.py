class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = { ')':'(', '}':'{',']':'['}
        st = []

        if len(s)<2:
            return False

        for ch in s:
            if ch in close_to_open:
                if not st or st[-1]!=close_to_open[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)
        
        if st:
            return False
        return True