import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets