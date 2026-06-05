class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        st = []
        for ch in operations:
            if ch=="+":
                st.append(st[-1]+st[-2])
            elif ch=="D":
                st.append(st[-1]*2)
            elif ch=="C":
                st.pop()
            else:
                st.append(int(ch))
        return sum(st)

        