def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_acceleration(speed, time):
        return speed / time