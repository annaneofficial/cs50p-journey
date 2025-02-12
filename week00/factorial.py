def factorial(n):
    if  n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    res = factorial(6)
    print(res)

main()
