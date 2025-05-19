class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        perv = [1, 1]
        for i in range(2, rowIndex + 1):
            new = [1 if c == 0 or c == i else 0 for c in range(i + 1)]
            for j in range(1, len(new) - 1):
                new[j] = perv[j - 1] + perv[j]
            perv = new
        return perv




s = Solution()
print(s.getRow(5))
