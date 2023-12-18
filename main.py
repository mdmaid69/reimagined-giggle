def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
n = 10
print("Square numbers:", [x**2 for x in range(n)])