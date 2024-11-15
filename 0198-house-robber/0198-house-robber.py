class Solution:
    def rob(self, nums: List[int]) -> int:
        robb1,robb2=0,0

        for n in nums:
            n=max(robb2, robb1+n)
            robb1=robb2
            robb2=n
        return robb2