# Solution 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if 'a' <= char <= 'z' or '0' <= char <= '9')
        return s == s[::-1]


# Solution 2

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = re.sub('[^a-z0-9]', '', s)
        return res == res[::-1]
