class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for strng in s:
            if strng.isalnum():
                newstr += strng.lower()
        return newstr==newstr[::-1]