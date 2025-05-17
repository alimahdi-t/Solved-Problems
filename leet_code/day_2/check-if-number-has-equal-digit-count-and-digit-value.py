class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(0, len(num)):
            # print(f"`{num[i]}` The digit {i} occurs {num[i]} times in num. -> {num[i] != num.count(str(i))}")
            if int(num[i]) != num.count(str(i)):
                return False
        return True


s = Solution()
print(s.digitCount("1210"))