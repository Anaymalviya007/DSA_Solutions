class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, value in enumerate(nums):
            valueToFind = target - value
            if valueToFind in hashMap:
                return [hashMap.get(valueToFind), index]

            hashMap[value] = index