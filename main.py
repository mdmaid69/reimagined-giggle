def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time