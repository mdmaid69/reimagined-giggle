def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_roi(gain, cost):
        return (gain - cost) / cost