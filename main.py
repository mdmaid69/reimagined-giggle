import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities