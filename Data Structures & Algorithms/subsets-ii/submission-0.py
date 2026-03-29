class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()

        def backtracking(i):
            
            if i == len(nums):
                res.append(sol[:])
                return

            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

            while i +1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # dont pick the number
            backtracking(i+1)
            
        backtracking(0)
        return res