import math


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        for i in range(min(min_num, max_num), 0, -1):
            if max_num % i == 0 and min_num % i == 0:
                return i
        return 1