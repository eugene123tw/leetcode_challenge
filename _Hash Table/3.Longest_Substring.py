# my solution
# Time limit exceeded
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#
#         buffer_list  = []
#         longest_list = []
#
#         for i in range(0,len(s)):
#             for j in range(i, len(s)):
#                 if s[j] not in buffer_list:
#                     buffer_list.append(s[j])
#                 else:
#                     if len(buffer_list) > len(longest_list):
#                         longest_list = buffer_list
#                     buffer_list = []
#                     break
#
#         if len(buffer_list) > len(longest_list):
#             longest_list = buffer_list
#
#         longest_num= len(longest_list)
#         return longest_num

# Optimized solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        maxlength = 0

        buffer_dict={}

        for i in range(0,len(s)):
            if s[i] in buffer_dict and start <= buffer_dict[s[i]]:
                start=buffer_dict[s[i]]+1
            else:
                maxlength = max(maxlength, i-start+1)
            buffer_dict[s[i]] = i


        return maxlength


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring("abc"))