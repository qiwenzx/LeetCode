class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # # Method 1
        # merged = sorted(nums1 + nums2)
        # n = len(merged)
        # if n % 2 == 1:  # odd length
        #     return float(merged[n // 2])
        # else:  # even length
        #     return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

        # Method 2: Find the largest in num1, and smallest in num2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            max_left1 = float("-inf") if i == 0 else nums1[i-1]
            min_right1 = float("inf") if i == m else nums1[i]

            max_left2 = float("-inf") if j == 0 else nums2[j-1]
            min_right2 = float("inf") if j == n else nums2[j]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return float(max(max_left1, max_left2))
            
            elif max_left1 > min_right2:
                right = i - 1
            else:
                left = i + 1


