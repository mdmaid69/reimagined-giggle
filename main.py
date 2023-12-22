n = 10
print("Cube numbers:", [x**3 for x in range(n)])
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])