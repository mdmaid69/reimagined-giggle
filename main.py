def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps