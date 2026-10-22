class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        left = 0

        while left + 2 < len(s):
            right = left + 2

            if (s[left] != s[left + 1] and s[left] != s[right] and s[left + 1] != s[right]):
                count += 1

            left += 1
        return count

        # max_str = ""

        # left = 0
        # right = left + 1

        # while left < right and right < len(s):
        #     max_le = 0
        #     if s[left] != s[right]:
        #         max_le = max(max_le, right - left + 1)
        #         right += 1
        #     else:
        #         left += 1
        #         right += 1
            
        #     if right - left + 1 > len(max_str):
        #         max_str = s[left:right + 1]

        # return max_str
