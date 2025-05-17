class Solution:
    def isHappy(self, n: int) -> bool:
        if 1 == n or n == 7:
            return True
        elif n <= 9:
            return False
        s = 0
        for i in str(n):
            s += int(i) ** 2
        return self.isHappy(s)


ss = Solution()
print(ss.isHappy(7))
