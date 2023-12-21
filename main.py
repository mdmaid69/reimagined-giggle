import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps