import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps