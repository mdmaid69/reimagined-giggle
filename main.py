def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps