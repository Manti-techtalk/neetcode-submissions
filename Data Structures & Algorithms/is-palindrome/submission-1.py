class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered ="".join([i for i in s if i.isalnum()])
        reverse = filtered[::-1]
        if reverse.lower() == filtered.lower():
            return True
        return False
