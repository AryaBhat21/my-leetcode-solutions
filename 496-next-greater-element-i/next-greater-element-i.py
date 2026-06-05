class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        for i in nums2:
            while st and i>st[-1]:
                prev=st.pop()
                d[prev]=i
            st.append(i)
        while st:
            d[st.pop()]=-1
        res = []
        for i in nums1:
            res.append(d[i])
        return res
