class Solution(object):
    def reverseWords(self, s):
        l = list(s)
        count = 0
        i = 0
        v = "aeiou"
        while i < len(l) and l[i] != " ":
            if l[i] in v:
                count += 1
            i += 1

        while i < len(l):
            i += 1
            left = i
            c = 0

            while i < len(l) and l[i] != " ":
                if l[i] in v:
                    c += 1
                    
                i += 1

            right = i - 1

            if c == count:
                while left < right:
                    l[left], l[right] = (
                        l[right], l[left]
                    )

                    left += 1
                    right -= 1
    
        return "".join(l)
        

        


        