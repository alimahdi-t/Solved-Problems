class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for num in range(left, right + 1):
            if "0" not in str(num):
                if all([num % int(c) == 0 for c in str(num)]):
                    arr.append(num)
        return arr
