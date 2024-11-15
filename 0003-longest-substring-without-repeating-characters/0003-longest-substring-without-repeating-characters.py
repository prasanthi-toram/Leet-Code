class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0

        seen=set()
        res=0
        for i  in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            res=max(res,len(seen))
        return res
