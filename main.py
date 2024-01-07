def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)