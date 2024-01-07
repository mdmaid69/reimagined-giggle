text = "Hello, world!"
print("Characters:", len(text))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])