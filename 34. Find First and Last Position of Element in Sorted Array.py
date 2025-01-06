class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # perform the binary search twice; one for the start index and one for the end index
        def binary_search(find_start: bool) -> int:
            start = 0
            end = len(nums) - 1
            ans = -1 # default if target is not found
            while (start <= end):
                mid = (start + end) // 2
                if (target < nums[mid]):
                    end = mid - 1
                elif (target > nums[mid]):
                    start = mid + 1
                else:
                    # potential ans found
                    ans = mid
                    if (find_start):
                        end = mid - 1
                    else:
                        start = mid + 1
            return ans
        
        start_index = binary_search(find_start = True)
        end_index = binary_search(find_start = False)
        return [start_index, end_index]
