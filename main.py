import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets