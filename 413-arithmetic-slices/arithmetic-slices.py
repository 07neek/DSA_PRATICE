class Solution:
    def f(self, length: int):
        return (length - 1) * (length - 2) // 2
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        left = 1
        count = 0
        while left < len(nums):
            l = left - 1
            right = left
            d = nums[right] - nums[l]

            while right < len(nums) and nums[right] - nums[right - 1] == d:
                right += 1
            
            length = right - l
            sum_val = self.f(length)
            count = count + sum_val

            left = right
        return count

            

        