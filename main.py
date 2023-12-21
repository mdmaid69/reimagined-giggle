def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities