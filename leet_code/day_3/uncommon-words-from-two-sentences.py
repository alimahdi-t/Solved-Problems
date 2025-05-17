from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        a = set()
        b = set()
        unwanted = set()
        for i, j in c1.items():
            if j == 1:
                a.add(i)
            else:
                unwanted.add(i)
        print("h1", a)
        for i, j in c2.items():
            if j <= 1:
                b.add(i)
            else:
                unwanted.add(i)
        print(b)

        return list((a | b).difference(a & b).difference(unwanted))


s = Solution()
print(s.uncommonFromSentences("s z z z s", "s z ejt"))
# print(s.uncommonFromSentences("this apple is sweet", "this apple is sour"))