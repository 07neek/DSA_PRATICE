class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = total = 0
        sub_num = {0:1}

        for i in nums:
            total += i

            if total - k in sub_num:
                count += sub_num[total - k]
            sub_num[total] = 1 + sub_num.get(total, 0)

        return count
        
          