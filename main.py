def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)