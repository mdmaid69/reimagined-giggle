import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities