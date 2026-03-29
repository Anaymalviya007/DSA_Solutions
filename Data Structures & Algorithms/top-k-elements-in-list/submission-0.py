class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # 1. Count frequency
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # 2. Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # 3. Collect top k
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res