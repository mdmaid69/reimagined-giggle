import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets