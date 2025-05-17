class Solution:
    def findMissingAndRepeatedValues(self, grid):
        ans = [0 for _ in range(2)]
        s = set()
        for row in grid:
            for item in row:
                if item in s:
                    ans[0] = item
                else:
                    s.add(item)
        for i in range(1, len(grid) ** 2 + 1):
            if i in s:
                continue
            else:
                ans[1] = i

        return ans


sol = Solution()

print(sol.findMissingAndRepeatedValues([[1, 3], [2, 2]]))