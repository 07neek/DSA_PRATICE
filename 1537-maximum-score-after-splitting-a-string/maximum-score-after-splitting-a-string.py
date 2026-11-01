class Solution:
    def maxScore(self, s: str) -> int:
        count_0 = max_count = 0
        count_1 = s.count("1")

        for right in range(len(s) - 1):
            count_0 += s[right] == "0"
            count_1 -= s[right] == "1"
            max_count = max(max_count, count_0 + count_1)

        return max_count

        