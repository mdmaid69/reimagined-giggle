n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])