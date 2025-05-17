from collections import Counter
class Solution:
    def commonChars(self, words):
        # Start with the character count of the first word
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        # Expand the characters based on their minimum frequency
        result = []
        for char, freq in common.items():
            result.extend([char] * freq)

        return result

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))
