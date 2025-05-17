class Solution:
    def repeatedCharacter(self, s: str) -> str:
        x = set()
        for i in s:
            if i in x:
                return i
            else:
                x.add(i)