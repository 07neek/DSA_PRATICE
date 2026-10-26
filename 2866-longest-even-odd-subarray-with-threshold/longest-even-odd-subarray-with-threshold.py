class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        r = 0
        for i in range(len(nums)):
            curr_c = 0
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                curr_c = 1
                for j in range(i + 1, len(nums)):
                    if (nums[j] % 2 == nums[j - 1] % 2) or nums[j] > threshold:
                        break
                    curr_c += 1
            r = max(r, curr_c)

        return r



