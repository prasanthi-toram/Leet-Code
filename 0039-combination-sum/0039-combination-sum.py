class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def rec(i,tar,curr):
            if tar==0:
                res.append(curr.copy())
                return
            if i>=len(nums) or tar<0:
                return
            curr.append(nums[i])
            rec(i,tar-nums[i],curr)
            curr.pop()
            rec(i+1,tar,curr)
        rec(0,target,[])
        return res
        