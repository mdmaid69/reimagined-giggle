def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])