def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)