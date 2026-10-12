class Solution(object):
    def removeElement(self, nums, val):
        # left = 0
        # s = []

        # while left < len(nums):
        #     if nums[left] != val:
        #         s.append(nums[left])
        #     left += 1
        # return len(s)

        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            

        return i