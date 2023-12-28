def is_even(n):
        return n % 2 == 0
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)