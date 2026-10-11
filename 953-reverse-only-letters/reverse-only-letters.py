class Solution(object):
    def reverseOnlyLetters(self, s):
        l = list(s)
        left = 0
        right = len(s) -1

        while left < right:
            if not l[left].isalpha():
                left += 1
            elif not l[right].isalpha():
                right -= 1
            else:
                l[left], l[right] = (
                    l[right], s[left]
                )

                left += 1
                right -= 1
        return "".join(l)
