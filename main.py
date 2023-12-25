def calculate_density(mass, volume):
        return mass / volume
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)