class Solution:
    def countKDifference(self, nums, k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans


s = Solution()

print(s.countKDifference([1,2,2,1], 1))