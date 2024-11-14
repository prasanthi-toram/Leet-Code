class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]*n
        for i in range(1,len(nums)):
            out[i]=out[i-1]*nums[i-1]
        suff=1
        print(out)
        for i in range(n-2,-1,-1):
            suff*=nums[i+1]
            out[i]*=suff
            # suff*=nums[i+1]
        return out
        