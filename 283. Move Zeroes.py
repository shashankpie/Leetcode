class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                # move all the non-zero elements to the front, utimately leaving the zero's at the end
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        return nums
