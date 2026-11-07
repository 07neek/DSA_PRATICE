class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+=sum(arr[i:j+1])
        return s
        # n = len(arr)
        # x = 0
        # if n % 2 != 0:
        #     x = sum(arr)
            
        # add_odd_elem = 0
        # for i in range(n-2):
        #     add_odd_elem += arr[i]
        #     while i in range(i + 1, i + 2):
        #         add_odd_elem += arr[i]

        # return add_odd_elem + (x * 2)

        
        
        
