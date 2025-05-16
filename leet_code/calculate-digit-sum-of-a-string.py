class Solution:
    def digitSum(self, s: str, k: int) -> str:
        count = 0
        ans = s
        m = 0
        a = ""
        if len(ans) <= k:
            return ans
        for i in range(len(ans)):
            m += int(s[i])
            count += 1
            if k == count or i == len(ans) - 1:
                a += str(m)
                count = 0
                m = 0
        ans = a
        if len(ans) > k:
            return self.digitSum(ans, k)
        else:
            return ans




s = Solution()
print(s.digitSum("11111222223", 3))
print(s.digitSum("233", 3))
print(s.digitSum("00000000", 3))


# class Solution:
#     def digitSum(self, s: str, k: int) -> str:
#         if len(s) <= k:
#             return s
#
#         parts = []
#         for i in range(0, len(s), k):
#             group = s[i:i + k]
#             digit_sum = sum(int(ch) for ch in group)
#             parts.append(str(digit_sum))
#
#         return self.digitSum("".join(parts), k)
