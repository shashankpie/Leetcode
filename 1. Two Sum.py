# Solutin 1 - Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 2 - Optimal
# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic[temp], i]
            else:
                dic[nums[i]] = i
