class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits2(self, n):

        sum = 0
        count = 31
        remain = n
        list = []
        while remain>0:
            if remain%2==0:
                list.append(0)
            else:
                list.append(1)
                sum = sum + 1 * 2 ** count
            remain = remain//2
            count = count -1
        return sum

    def reverseBits(self, n):
        result = 0
        mask = 1
        for i in range(32):
            result <<= 1
            result |= n&mask
            n>>=1
        return result

if __name__ == "__main__":
    n = 43261596
    obj = Solution()
    print(obj.reverseBits(n))