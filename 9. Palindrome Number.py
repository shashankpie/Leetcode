class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev_num = 0
        if x < 0:
            return False
        else:
            while (x > 0):
                last_digit = x % 10
                rev_num = (rev_num * 10) + last_digit
                x = x // 10
            if temp == rev_num:
                return True
