class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findsearch(isFirst: bool) -> int:
            left = 0
            right = len(nums) - 1
            indice = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    indice = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return indice
        return [findsearch(True), findsearch(False)]
            