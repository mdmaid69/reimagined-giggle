def calculate_energy(mass, c=3*10**8):
        return mass * c**2
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))