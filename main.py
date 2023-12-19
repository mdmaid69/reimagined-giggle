def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)