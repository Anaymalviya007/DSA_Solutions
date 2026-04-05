class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(arr):
            n = len(arr)
            
            if n == 1:
                return arr[0]
            
            memo = {0: arr[0], 1: max(arr[0], arr[1])}
            
            def check_rob(i):
                if i in memo:
                    return memo[i]
                
                memo[i] = max(arr[i] + check_rob(i-2), check_rob(i-1))
                return memo[i]
            
            return check_rob(n-1)
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        # Case 1: skip last
        case1 = solve(nums[:-1])
        
        # Case 2: skip first
        case2 = solve(nums[1:])
        
        return max(case1, case2)