def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)