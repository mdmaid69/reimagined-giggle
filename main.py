print([x**2 for x in range(10)])
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)