class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtracking(i):
            if i == n:
                res.append(sol[:]) # appending the copy of sol using [:]
                return

            # dont pick the number at i 
            backtracking(i + 1)

            # pick the number at i
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
            
        backtracking(0)

        return res