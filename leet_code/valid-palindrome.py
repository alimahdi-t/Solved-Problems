class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s.lower():
            if i.isalnum():
                x += i
        return x == x[::-1]


# second solution
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         x = [c for c in s.lower() if c.isalnum()]
#         return x == x[::-1]
