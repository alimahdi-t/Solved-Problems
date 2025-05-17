# from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # counts = Counter(s)
        # print(counts)
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        k = d.get(s[0])
        return all(o == k for o in d.values())



sol = Solution()
print(sol.areOccurrencesEqual("abacbc"))
print(sol.areOccurrencesEqual("aaabb"))

