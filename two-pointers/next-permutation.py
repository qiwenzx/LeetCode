class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Find the first decending element
        i = n - 2
        while i >= 0 and nums[i] > nums[i+1]:
            i = i - 1
        
        # Find the element just larger than num[i]
        if i >=0:
            j = n - 1
            while nums[j] < nums[i]:
                j = j - 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the order
        nums[i+1:] = reversed(nums[i+1:])
        
        