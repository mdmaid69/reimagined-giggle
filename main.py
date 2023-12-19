def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)