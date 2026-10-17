class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0 
        m_l = 0
        elem = set()

        for j in range(len(s)):
            while s[j] in elem:
                elem.remove(s[left])
                left += 1
            
            elem.add(s[j])
            m_l = max(m_l, j - left + 1)

        return m_l

        # r = []        
        # left = 0
        # right = left + 1
        # while left < right and right < len(s):
        #     if s[left] != s[right]:
        #         r.append(s[right])
        #         right += 1
        #     elif s[left] == s[right]:

        #         if s[right] in r:
        #             r.remove(s[right])

        #         left = right
        #         right += 1

        # return len(r)
