class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        k=k%len(nums)
        nums[:]=nums[-k:] + nums[:-k]
        # while i<k:
        #     nums=[nums[-1]]+nums
        #     nums.pop()
        #     i+=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        