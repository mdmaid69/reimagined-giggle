def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities