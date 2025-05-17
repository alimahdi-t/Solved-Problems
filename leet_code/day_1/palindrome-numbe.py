class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     return str(x) == str(x)[::-1]

    # using math
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


s = Solution()
print(s.isPalindrome(121))
