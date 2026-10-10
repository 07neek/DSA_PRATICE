class Solution(object):
    def twoSum(self, nums, target):

        # right = len(nums) - 1
        # nums.sort()

        # for left in range(len(nums)- 2):

        #    while left < right:
        #         sum = nums[left] + nums[right]

        #         if sum == target:
        #             return [left, right]
        #         elif sum < target:
        #             left += 1
        #         else:
        #             right -= 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
                

                

        