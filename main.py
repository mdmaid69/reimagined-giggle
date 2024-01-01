def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)