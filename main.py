import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity