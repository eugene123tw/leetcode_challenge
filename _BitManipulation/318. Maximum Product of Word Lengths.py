def str2binary(str):
    result = 0
    for char_ in str:
        result |= 1 << ord(char_) - 97+26
    return result

class Solution(object):
    def maxProduct(self, words):
        max_len = 0

        value = [0]*len(words)

        for i in range(len(words)):
            value[i] = str2binary(words[i])


        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if value[i] & value[j] == 0 :
                    if len(words[i])*len(words[j])>max_len:
                        max_len = len(words[i])*len(words[j])

        return max_len


if __name__ == '__main__':
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    obj = Solution()
    print(obj.maxProduct(words))