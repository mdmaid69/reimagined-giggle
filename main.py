x = 10
y = 20
print("Sum:", x + y)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)