class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            a = 2 ** i
            if a == n:
                return True
        return False
