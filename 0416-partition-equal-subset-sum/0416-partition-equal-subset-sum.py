class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)

        if summ%2!=0:
            return False
        target=summ//2

        n=len(nums)

        memo = [[False]*(target+1) for i in range(n)]

        for i in range(n):
            memo[i][0]=True
        # memo[0][nums[0]]=True
        
        for  i in range(1,n):
            for j in range(1,target+1):
                if nums[i]<=j:
                    memo[i][j]= memo[i-1][j] or memo[i-1][j-nums[i]]
                else:
                    memo[i][j]= memo[i-1][j]
        return memo[n-1][target]
                    
        