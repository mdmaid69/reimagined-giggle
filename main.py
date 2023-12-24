def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps