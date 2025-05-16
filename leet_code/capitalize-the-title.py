class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([i.lower() if len(i) <= 2 else i.lower().capitalize() for i in title.split()])


s = Solution()
print(s.capitalizeTitle("capiTalIze OF tHe titLe"))