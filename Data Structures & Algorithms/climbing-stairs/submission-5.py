class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def f(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = f(i-2) + f(i-1)
                return memo[i]
                
        return f(n)
