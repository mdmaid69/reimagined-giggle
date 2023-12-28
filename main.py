def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_acceleration(speed, time):
        return speed / time