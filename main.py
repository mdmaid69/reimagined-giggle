def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time