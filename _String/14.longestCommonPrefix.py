# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         common_prefix = ""
#
#         min = 100000
#         cnt = 0
#         for item in strs:
#             if len(item)<=min:
#                 min = len(item)
#
#         if len(strs)==1:
#             return strs
#
#         for j in range(0,min):
#             for i in range(1, len(strs)):
#                 if strs[0][j]!=strs[i][j]:
#                     return common_prefix
#
#                 cnt+=1
#
#                 if cnt==(len(strs)-1):
#                     common_prefix += strs[0][j]
#                     cnt=0
#
#         return common_prefix

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

if __name__ == "__main__":

    strs = ['abcd','abccc','abdec']
    # strs = ['a']

    obj = Solution()
    print(obj.longestCommonPrefix(strs))