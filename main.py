def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import json
def convert_to_json(data):
        return json.dumps(data)