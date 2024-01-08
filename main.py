def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)