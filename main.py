n = 10
print("Powers of 2:", [2**x for x in range(n)])
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])