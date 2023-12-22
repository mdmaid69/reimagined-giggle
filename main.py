def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time