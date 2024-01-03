def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)