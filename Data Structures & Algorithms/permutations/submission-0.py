class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(path):
            # Base case: all numbers are used
            if len(path) == len(nums):
                result.append(path[:])  # Add a copy of path
                return
            
            # Try each number that hasn't been used
            for num in nums:
                if num not in path:
                    path.append(num)          # Choose
                    backtrack(path)           # Explore
                    path.pop()                # Unchoose (Backtrack)
        
        backtrack([])
        return result
