class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        check = []
        left = 0
        count = {}
        for right in range(9, len(s)):
            x = s[left:right + 1]
            if x not in count:
                count[x] = 1
            else:
                if count[x] == 1:
                    check.append(x[:])
                    count[x] += 1

            left += 1

        return check

