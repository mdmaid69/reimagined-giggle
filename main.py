def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)