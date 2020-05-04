def Fibonacci(n):
    sum, first, second = 0, 1, 1
    for i in range(n):
        sum = first + second
        first = second
        second = sum
        print(sum)

if __name__ == '__main__':
    Fibonacci(5)