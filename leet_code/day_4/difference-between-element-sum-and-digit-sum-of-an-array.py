class Solution:
    def differenceOfSum(self, nums) -> int:
        element_sum = sum(nums)
        d = "".join([str(c) for c in nums])
        digit_sum = 0
        for i in d:
            digit_sum += int(i)

        return abs(digit_sum - element_sum)


s = Solution()

print(s.differenceOfSum([1,15,6,3]))