class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        dp[0]=1
        if s[0]!='0':
            dp[1]=1
        for i in range(1,len(s)):
            if s[i]>'0' :
                dp[i+1]+=dp[i]
            if s[i-1]+s[i] < '27' and s[i-1]+s[i] > '09':
                dp[i+1]+=dp[i-1]
        return dp[-1]
        