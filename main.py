n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)