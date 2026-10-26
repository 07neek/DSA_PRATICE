class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c = 0
        left = 0
        right = k 
        s = str(num)

        while right <= len(s):
            if int(s[left:right]) != 0 and  num % int(s[left:right]) == 0:
                c += 1
            
            left += 1
            right += 1

        return c
        # if len(str(num)) < 2 and k == 1:
        #     return 1
        # left = 0
        # right = left + 1
        # divisor_c = 0
        # if k >= 2:
        #     while left < right and right < len(str(num)):
        #         s = str(num)
        #         x = s[left] + s[right]
        #         try:
        #             if num % int(x) == 0:
        #                 divisor_c += 1
        #         except ZeroDivisionError:
        #             None

        #         left = right
        #         right += 1
        # else:
        #     s = str(num)
            
        #     for i in s:
        #         try:
        #             if num % int(i) == 0:
        #                 divisor_c += 1
        #         except ZeroDivisionError:
        #             None
            
        return divisor_c

        