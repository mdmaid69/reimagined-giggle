import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets