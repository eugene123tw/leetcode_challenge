def perm(strs,buffer_str,empty_list):
    for i in strs[0]:
        if len(strs)>1:
            perm(strs[1:],buffer_str+i,empty_list)
        else:
            empty_list.append(buffer_str+i)
    return empty_list

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        empty_list = []
        strs = []

        phone_dict={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        if len(digits) == 0:
            return empty_list

        if len(digits) == 1:
            return phone_dict[digits]


        for index in digits:
            strs.append(phone_dict[index])

        empty_list = perm(strs,"",empty_list)

        return empty_list

if __name__ == '__main__':
    obj = Solution()
    print(obj.letterCombinations("2"))
