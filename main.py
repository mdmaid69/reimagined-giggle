def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
n = 10
print("Powers of 2:", [2**x for x in range(n)])