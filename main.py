def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps