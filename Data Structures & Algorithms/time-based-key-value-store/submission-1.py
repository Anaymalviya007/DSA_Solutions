class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        retrived_tuples = self.store[key]
        # [(),(),()]
        left = 0
        right = len(retrived_tuples)-1

        while left <=right:
            mid = (left+right)//2

            if retrived_tuples[mid][0] == timestamp:
                return retrived_tuples[mid][1]

            if timestamp >= retrived_tuples[mid][0]:
                
                left = mid +1
            else:
                right = mid -1
        if right >= 0:
            return retrived_tuples[right][1]
            
        return ""


