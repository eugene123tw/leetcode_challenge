class Solution(object):
    def reverse(self, x):
        rev = 0

        negative = False
        if x < 0 :
            negative = True
            x = 0-x

        while x!=0:
            rev = rev*10+ x%10
            x = x//10

            if rev > (2**31)-1:
                return 0

        if negative:
            rev = 0-rev

        return rev


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse(-123))