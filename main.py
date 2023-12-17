def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2