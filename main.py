import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets