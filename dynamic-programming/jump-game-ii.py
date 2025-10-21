class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        # we stop before last index; when we reach or pass it, we’re done
        for i in range(len(nums) - 1):
            # best reach from current position
            farthest = max(farthest, i + nums[i])

            # time to make a jump
            if i == end:
                jumps += 1
                end = farthest

        return jumps