class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones] 
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x != y:
                res = x-y
                heapq.heappush(max_heap, -res)
            
        if max_heap:
            return -max_heap[0]
        return 0            
        
