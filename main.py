def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"