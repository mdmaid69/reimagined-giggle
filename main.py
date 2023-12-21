print([x**2 for x in range(10)])
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)