def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)