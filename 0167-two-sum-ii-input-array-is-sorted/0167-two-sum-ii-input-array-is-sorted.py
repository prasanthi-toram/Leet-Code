class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1

        while i<j:

            summ = numbers[i]+numbers[j]
            if summ <target:
                i+=1
            elif summ > target:
                j-=1
            
            else:
                # print (i)
                # print(j)
                return [i+1,j+1]
        return[]