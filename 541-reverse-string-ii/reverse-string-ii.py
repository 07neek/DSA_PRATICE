class Solution(object):
    def reverseStr(self, s, k):
        #brute force
        # r = ""
        # for i in range(0, len(s), 2*k):
        #     r += s[i:i+k][::-1]
        #     r += s[i+k:i + 2*k]
        # return r

        #two pointers
        l = list(s)
        
        for start in range(0, len(s), 2*k):
            left = start
            right = min(start + k - 1, len(s)-1)

            while left < right:
                l[left], l[right] = (
                    l[right], l[left]
                )

                left += 1
                right -= 1

        return "".join(l)