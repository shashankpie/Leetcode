# Brute force Solution - Time limit exceeded

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for ele in nums:
            cnt = 0
            for j in range(len(nums)):
                if ele == nums[j]:
                    cnt += 1
            if cnt > (len(nums) // 2):
                return ele
        return -1
