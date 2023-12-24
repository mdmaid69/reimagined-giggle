import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps