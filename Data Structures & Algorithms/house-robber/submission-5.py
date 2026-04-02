class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1],nums[0])
        memo = {0:nums[0], 1:max(nums[1],nums[0])}
        def check_rob(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+check_rob(i-2), check_rob(i-1))
                return memo[i]
        
        return check_rob(n-1)
