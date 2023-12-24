import random
def generate_random_number(start, end):
        return random.randint(start, end)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities