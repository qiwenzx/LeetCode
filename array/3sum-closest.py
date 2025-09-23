class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float("inf")
        result = 0

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < closest:
                    closest = abs(total - target)
                    result = total

                if total < target:
                    left = left + 1
                elif total > target:
                    right = right - 1
                else:
                    return total
        return result