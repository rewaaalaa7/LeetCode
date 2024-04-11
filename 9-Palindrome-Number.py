class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        return True if lst == lst[::-1] else False