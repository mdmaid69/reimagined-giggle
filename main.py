from collections import Counter
print(Counter("hello world"))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])