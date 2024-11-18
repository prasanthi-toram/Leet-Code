class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict [num] = 1 + nums_dict .get(num, 0)
        print (nums_dict)

        freq=[[] for i in range(len(nums)+1)]

        for num,cnt in nums_dict.items():
            freq[cnt].append(num)
        res=[]

        for j in range(len(freq)-1,0,-1):
            for p in freq[j]:
                res.append(p)
            if len(res)==k:
                return res
            
        
        
        