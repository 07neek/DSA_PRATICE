class Solution(object):
    def canChange(self, start, target):
        right = 0
        left = 0
        n = len(start)

        while left < n or right < n:
            while left < n and start[left] == "_":
                left += 1
            
            while right < n and target[right] == "_":
                right += 1

            if left == n or right == n:
                return (left==n and right==n)

            if start[left] != target[right] or (start[left] == "L" and right > left) or (start[left] == "R" and right < left):
                return False

            left += 1
            right += 1

        return True
        