def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities