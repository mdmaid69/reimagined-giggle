import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities