import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity