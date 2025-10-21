class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            # if we reach a point that is not reachable
            if i > farthest:
                return False
            # update the farthest reachable index
            farthest = max(farthest, i + nums[i])
        return True