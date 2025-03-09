class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        i = 0  # Slow pointer (insertion position)
        
        for num in nums:
            # Allow at most 2 occurrences of each number
            if i < 2 or num != nums[i - 2]: 
                nums[i] = num
                i += 1
                
        return i  # New length of the array

        # i,j=0,0

        # k=0

        # while i<len(nums) and  j<len(nums):
        #     if nums[i]==nums[j]:
        #         if k<2:
        #             j+=1
        #             # i+=1
        #             # i+=1
        #             k+=1
        #         else:
        #             j+=1
        #     else:
        #         if k>=2:
        #             i+=2
        #             nums[i]=nums[j]
        #             # i+=1
        #             # j+=1
        #             k=0
        #         else:
        #             i=j
        #             k=0

        # return i+1

        # # while i<len(nums) and j<len(nums):
        # #     k=0
        # #     while k
        # #     if 