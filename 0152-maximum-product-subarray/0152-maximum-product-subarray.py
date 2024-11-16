class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftprod=1
        rightprod=1
        maxprod= float('-inf')

        l,r =0,len(nums)-1

        while l<len(nums) and r>=0:
            leftprod*=nums[l]
            rightprod*=nums[r]

            maxprod=max(maxprod,leftprod,rightprod)

            if leftprod==0:
                leftprod=1
            if rightprod==0:
                rightprod=1
            l+=1
            r-=1
        return maxprod

        