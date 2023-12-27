def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)