class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}

        for index, item in enumerate(nums):
            diffrence = target - item

            if diffrence in hasmap:
                return [hasmap[diffrence],index]
            
            hasmap[item] = index
        return []