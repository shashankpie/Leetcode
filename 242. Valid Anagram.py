# Solution 1
# Time complexity - O(nlog(n))
# Space complexity - O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True                
        else:
            return False


# Solution 2
# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
