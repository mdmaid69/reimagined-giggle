def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
n = 10
print("Powers of 2:", [2**x for x in range(n)])