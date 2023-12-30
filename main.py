n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])