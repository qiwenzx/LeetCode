class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                results.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue


                val = candidates[i]
                path.append(val)

                backtrack(i+1, path, total + val)
                path.pop()

        backtrack(0, [], 0)
        return results