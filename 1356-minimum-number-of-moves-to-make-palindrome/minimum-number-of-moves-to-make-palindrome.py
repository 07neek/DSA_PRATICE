class Solution(object):
    def minMovesToMakePalindrome(self, s):
        l = list(s)
        count = 0
        i, j = 0, len(s) - 1

        while i < j:
            r = j
            while r > i and l[r] != l[i]:
                r -= 1
                
            if r != i:
                while r < j:
                    l[r], l[r+1] = (
                        l[r+1], l[r]
                    )
                    count += 1
                    r += 1
            else:
                l[r], l[r+1] = l[r+1], l[r]
                count += 1
                continue
            i += 1
            j -= 1


        return count