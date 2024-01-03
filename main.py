import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps