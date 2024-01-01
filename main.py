n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])