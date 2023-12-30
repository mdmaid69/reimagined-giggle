def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_perpetuity(payment, rate):
        return payment / rate