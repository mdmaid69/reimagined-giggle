def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import random
def generate_random_choice(choices):
        return random.choice(choices)