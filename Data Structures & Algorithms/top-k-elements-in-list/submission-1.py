class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequency map
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n,0) + 1

        print(frequency)

        # now frequency is create and it will look like this {1:1, 2:2, 3:3}
        # now we have to create buckets to store the occurence of the element 

        buckets = [[] for _ in range(len(nums) + 1)] # +1 is because we need 6 places to store the occcurence for example 1
        print(buckets)
        for num, count in frequency.items():
            buckets[count].append(num)
        print(buckets)
        # now our buckets is ready and it will look somting like this [[], [1], [2], [3], [], [], []]
        # see each index is the occurence of that element 
        # now we just need to itrate in reverce and print the k element 
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result