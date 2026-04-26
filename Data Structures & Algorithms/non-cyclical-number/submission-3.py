class Solution:
    def get_next(self, n):
        return sum(int(i)**2 for i in str(n))

    def isHappy(self, n: int) -> bool:
        slow = n 
        fast = self.get_next(n) 

        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return fast == 1

