import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities