class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ele in t:
            if ele not in s:
                return ele
            else:
                if s.count(ele) != t.count(ele):
                    return ele
