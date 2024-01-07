def calculate_energy(mass, c=3*10**8):
        return mass * c**2
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)