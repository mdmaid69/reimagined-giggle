from collections import Counter
print(Counter("hello world"))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)