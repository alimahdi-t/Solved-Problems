class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = []
        for i in range(0, len(s), k):
            arr.append(s[i: i + k])

        last_element = arr[-1]
        if len(last_element) < k:
            print("ehy")
            arr[-1] = f"{last_element}{(k - len(last_element)) * fill}"
        return arr