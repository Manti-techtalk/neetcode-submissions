class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter the string to include only alphanumeric characters and make it lowercase
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Create the reversed string
        _ls = filtered_s[::-1]
        
        # Step 3: Compare the filtered string with its reverse
        return filtered_s == _ls
