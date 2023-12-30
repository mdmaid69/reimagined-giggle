def calculate_force(mass, acceleration):
        return mass * acceleration
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)