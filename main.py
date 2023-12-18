def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)