class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums= set(nums)
        
        res=0

        for num in nums:
            streak=0
            if num-1 in set_nums:
                continue
            curr = num
            while curr in set_nums:
                streak+=1
                curr+=1
            res=max(streak,res)
        return res

        
        