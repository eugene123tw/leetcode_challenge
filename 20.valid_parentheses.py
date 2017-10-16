class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack==[] or stack.pop()!=dict[char]:
                    return False
            else:
                return False
        return stack == []


if __name__ == '__main__':

    # s = "(["
    s = "()[]{}"
    # s = "[({})]"
    # s = "[({})}"
    # s = "[)[]{}"
    # s = "(()("
    obj = Solution()
    print(obj.isValid(s))
    pass
