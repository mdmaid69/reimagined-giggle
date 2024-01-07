import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))