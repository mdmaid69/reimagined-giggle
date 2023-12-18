def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time