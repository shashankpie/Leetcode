class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            ele = nums[i]
            if ele < 0:
                ele = ele * -1
            if len(str(ele)) % 2 == 0:
                count += 1
        return count
