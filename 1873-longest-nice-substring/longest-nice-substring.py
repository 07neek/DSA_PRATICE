class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        max_str = ""

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                elem = set(s[left:right + 1])

                nice = True

                for ele in elem:
                    if ele.lower() not in elem or ele.upper() not in elem:
                        nice = False
                        break
                
                if nice and right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]
        return max_str
        # x = s.lower()
        # left = 0
        # right = left + 1
        # m_l = 0
        # r = ""
        
        # while left < right and right < len(s):
        #     if x[left] != x[right]:
        #         left = right
        #         right += 1
        #     elif x[left] == x[right]:
        #         m_l = max(m_l, right - left + 1)
        #         right += 1
            
        # return s[m_l:]

        