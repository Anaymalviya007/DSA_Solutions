
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Stores the maximum sum found
        curr_sum = 0  # Stores the sum of the current subarray

        for num in nums:
            curr_sum = max(num, curr_sum + num)  # Continue or restart subarray
            max_sum = max(max_sum, curr_sum)  # Update max_sum if needed

        return max_sum