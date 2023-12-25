def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])