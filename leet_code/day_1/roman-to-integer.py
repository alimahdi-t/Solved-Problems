class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000

        }
        ans = 0
        i = 0
        length = len(s)
        while i < length:
            if i + 1 < length and d[s[i]] < d[s[i + 1]]:
                ans += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans


s = Solution()
print(s.romanToInt("III"))  # 3
print(s.romanToInt("LVIII"))  # 58
print(s.romanToInt("MCMXCIV"))  # 1994
