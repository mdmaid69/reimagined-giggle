import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding