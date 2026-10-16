class Solution(object):
    def findMaxAverage(self, nums, k):
        
        max_sum = sum(nums[:k])
        cur_sum = max_sum

        for i in range(k, len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i - k]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return float(max_sum) / k
        
        # max_sum = 0
        # for i in range(0, len(nums) - k + 1):
        #     left = i
        #     left_f = left + 1

        #     cur_sum = nums[left]
        #     while left_f < left + k:
        #         cur_sum += nums[left_f]

        #         left_f += 1

        #     if cur_sum > max_sum:
        #         max_sum = cur_sum

        # return float(max_sum) / k

