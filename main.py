def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)