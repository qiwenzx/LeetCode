class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            # base case: path complete
            if len(path) == len(nums):
                res.append(path[:])   # make a copy
                return

            for n in nums:
                if n not in path:     # skip already used numbers
                    path.append(n)
                    backtrack(path)
                    path.pop()        # undo the last choice (backtrack)

        backtrack([])
        return res