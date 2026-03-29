class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = nums + nums
        print(ans)
        
        for i, v in enumerate(range(n)):
            if ans[i] != nums[i]:
                return False
            if ans[i + n] != nums[i]:
                return False
            n +=1
            return ans
        
        return False