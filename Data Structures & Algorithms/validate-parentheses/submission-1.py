class Solution:
    def isValid(self, s: str) -> bool:
        rounded = '()'
        brackets = '{}'
        square = '[]'
        while rounded in s or brackets in s or square in s:
            s = s.replace(rounded, '')
            s = s.replace(brackets,'')
            s = s.replace(square,'')
        return s == ''
