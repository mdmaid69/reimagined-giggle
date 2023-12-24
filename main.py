import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities