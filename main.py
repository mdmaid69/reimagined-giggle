def calculate_perpetuity(payment, rate):
        return payment / rate
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)