import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities