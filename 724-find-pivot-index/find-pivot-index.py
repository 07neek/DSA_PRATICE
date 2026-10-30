class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_t = 0

        for i in range(len(nums)):
            
            right_t = total - left_t - nums[i]
            if right_t == left_t:
                return i
            else:
                left_t += nums[i]

        return -1
        