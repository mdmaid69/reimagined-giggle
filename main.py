def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)