import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps