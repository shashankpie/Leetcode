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


# Optimal Solution - Moore’s Voting Algorithm
# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = nums[0]
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                ele = nums[i]
            elif ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = 0
        for i in range(len(nums)):
            if ele == nums[i]:
                cnt1 += 1
        if cnt1 > len(nums) // 2:
            return ele
        return -1
