class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # dp[i] = number of ways to decode first i characters
        dp = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, n + 1):
            # one digit (last character)
            one_digit = int(s[i - 1:i])
            
            # two digits (last two characters)
            two_digits = int(s[i - 2:i])
            
            # if valid single digit (1-9)
            if one_digit >= 1:
                dp[i] += dp[i - 1]
            
            # if valid two digits (10-26)
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]