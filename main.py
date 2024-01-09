n = 10
print("Cube numbers:", [x**3 for x in range(n)])
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)