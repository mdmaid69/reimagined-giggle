def calculate_energy(mass, c=3*10**8):
        return mass * c**2
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)