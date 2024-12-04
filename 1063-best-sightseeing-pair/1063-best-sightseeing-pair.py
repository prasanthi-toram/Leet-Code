
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp=[0]*len(values)
        maxvalue=0

        for i in range(1,len(values)):
            dp[i]=max(dp[i-1], values[i-1]+i-1)
            maxvalue=max(maxvalue,dp[i]+values[i]-i)
        return maxvalue