import random
print(random.randint(0, 100))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)