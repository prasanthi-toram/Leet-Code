class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        bestl=0
        betsr=0
        longest_len=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)>longest_len:
                    bestl=l
                    bestr=r
                    longest_len= r-l+1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)>longest_len:
                    bestl=l
                    bestr=r
                    longest_len= r-l+1
                l-=1
                r+=1
        return s[bestl:bestr+1]
            
