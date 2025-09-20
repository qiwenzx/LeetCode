class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # Method 1(Brute force)
        # n = len(height)
        # max_area = 0

        # for i in range(n):
        #     for j in range(i+1, n):
        #         area = (j - i) * min(height[i], height[j])
        #         max_area = max(max_area, area)

        # return max_area

        # Method 2
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area
