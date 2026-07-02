'''
1. Input --> String
2. Output --> boolean : True or False
3. True if it is a palindrome, falls if not
4. Ignore all non-alphanumeric characters
PROCUDE
1. Extract only the alphhanemric char
2. Chech the front if the same as the back
3. If the same return True, otherwise false
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        return res == res[::-1]
        