class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isvalid = True
        for i in s:
            print(i, isvalid)
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    isvalid = False
                    break
                popped = stack.pop()
                if popped == "(":
                    if i != ")":
                        return False
                elif popped == "[":
                    if i != "]":
                        return False
                elif popped == "{":
                    if i != "}":
                        return False
        return isvalid and len(stack) == 0


s = Solution()
print(s.isValid("()[]{}"))


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         bracket_map = {')': '(', ']': '[', '}': '{'}
#
#         for char in s:
#             if char in bracket_map.values():  # Opening brackets
#                 stack.append(char)
#             elif char in bracket_map:  # Closing brackets
#                 if not stack or stack.pop() != bracket_map[char]:
#                     return False
#             else:
#                 # If you want to ignore invalid characters, otherwise return False
#                 return False
#
#         return len(stack) == 0
