class Solution(object):
    def removeDuplicates(self, nums):
        # slow = 0 
        # c_dup = 0

        # for j in range(1, len(nums), 2):
        #     if nums[j] == nums[slow]:
        #         c_dup += 1
        #         slow = j + 1     
        #     elif nums[j] != nums[slow]:
        #         slow += 1
        #         nums[slow] = nums[j]

        j, c = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                c += 1
            else:
                c = 1
            
            if c <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j

            
            
        