def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)