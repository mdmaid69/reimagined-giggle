def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps