def calculate_pressure(force, area):
        return force / area
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)