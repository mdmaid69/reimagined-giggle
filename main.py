import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))