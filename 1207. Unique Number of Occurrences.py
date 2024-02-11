class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the number of occurrences
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        # Check whether that number is unique
        seen = set()
        for key, value in dic.items():
            if value in seen:
                return False
            else:
                seen.add(value)
        return True
