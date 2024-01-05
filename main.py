def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)