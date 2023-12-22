def add_numbers(x, y):
        return x + y
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)