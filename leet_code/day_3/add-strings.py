class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            num2 = num2.zfill(l1)
        else:
            num1 = num1.zfill(l2)
        print(num1)
        print(num2)
        carry = 0
        result = []
        for i in range(len(num1) - 1, -1, -1): # go to -1 so the index 0 included
            total = (int(num1[i]) + int(num2[i]) + carry)
            carry, digit = divmod(total, 10)
            result.append(str(digit))

        if carry:
            result.append(str(carry))

        return "".join(reversed(result))





sol = Solution()
print(sol.addStrings("0012", "1245"))
