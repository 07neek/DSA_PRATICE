class Solution(object):
    def reverseWords(self, s):
        f = []
        right = len(s) - 1

        while right >= 0:
            if s[right] == " ":
                right -= 1
                continue

            left = right

            while left >= 0 and s[left] != " ":
                left -= 1

            f.append(s[left + 1:right+1])

            right = left

        return " ".join(f)
        