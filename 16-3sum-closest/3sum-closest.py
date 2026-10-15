class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result
        # i = 0
        # j = i + 1
        # k = j + 1
        # sum = 0

        # for i in range()
        # while i < j < k and k < len(nums):
        #     x = abs(nums[i] + nums[j] + nums[k])
        #     if  x <= target or x >= target:
        #         sum = x
        #         i += 1
        #         j += 1
        #         k += 1 
        #     else:
        #         i += 1
        #         j += 1
        #         k += 1  

        # return sum         