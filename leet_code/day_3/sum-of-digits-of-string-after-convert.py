class Solution:
    def getLucky(self, s: str, k: int) -> int:
        x = ""
        for i in s:
            x += str(ord(i) - 96)
        while k > 0:
            x = sum([int(c) for c in str(x)])
            k -= 1
        return x


sol = Solution()
print(sol.getLucky("leetcode", 2))
