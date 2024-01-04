def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def calculate_energy(mass, c=3*10**8):
        return mass * c**2