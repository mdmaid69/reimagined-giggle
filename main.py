import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets