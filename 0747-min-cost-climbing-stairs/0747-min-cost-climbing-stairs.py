class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        a=[0]*(n+1)
        # a[0],a[1] =
        if not cost :
            return 0
        elif len(cost)==1:
            return cost[0]
        else:
            for j in range(2,len(cost)+1):
                a[j]= min((a[j-1]+cost[j-1]), (a[j-2]+cost[j-2]))
        print (a)
        return a[-1]


