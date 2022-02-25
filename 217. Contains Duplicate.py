class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # why hashset? cause, faster lookup time.
        for num in nums:
            if num in hashset:
                return True
            else: # if num doesn't exist in hashset then add.
                hashset.add(num)
        return False # if it doesn't return True and only adds the items to the hashset.
