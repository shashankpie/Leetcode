class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def findPeakElement():
            start = 0
            end = mountainArr.length() - 1
            while (start < end):
                mid = (start + end) // 2
                if (mountainArr.get(mid) > mountainArr.get(mid+1)):
                    # potential ans
                    end = mid
                else:
                    start = mid + 1
            return end

        def binary_search(start: int, end: int, ascending: bool) -> int:
            while start <= end:
                mid = (start + end) // 2
                value = mountainArr.get(mid)
                if value == target:
                    return mid  # Return immediately when found
                if ascending:
                    if value < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if value > target:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1  # Return -1 if target is not found
        
        peak = findPeakElement()

        # Search in the ascending part
        result = binary_search(0, peak, ascending=True)
        if result != -1:
            return result

        # Search in the descending part
        return binary_search(peak + 1, mountainArr.length() - 1, ascending=False)
