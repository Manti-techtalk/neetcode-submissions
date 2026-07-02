class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [char.lower() for char in s if char.isalnum()]
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        