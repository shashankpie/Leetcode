class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while (start < end):
            mid = (start + end) // 2
            if (nums[mid] > nums[mid+1]):
                # this may be the answer
                # we are in the decreasing part of the array
                end = mid
                # because we still have to check mid-1 (left) element to confirm
            else:
                start = mid + 1
        # the above two checks are performing to find the largest element
        # if largest element found in first check and second check are same, then the largest element is found; if start == end
        return start # or return end // because both have same value
