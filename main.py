def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b