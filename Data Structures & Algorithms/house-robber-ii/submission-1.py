class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(arr):
            prev2 = 0
            prev1 = 0
            
            for num in arr:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        # Case 1: skip last
        case1 = rob_linear(nums[:-1])
        
        # Case 2: skip first
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2)