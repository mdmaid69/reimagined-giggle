def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)